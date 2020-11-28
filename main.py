import requests
import os
import json
import secrets
import psycopg2

# A Twitter API bearer token is required to run this script, it is expected
# that the bearer token is stored in secrets.py in the same directory, and
# is set as follows:
# BEARER_TOKEN = <your bearer token>

def auth():
    return secrets.BEARER_TOKEN

def create_url(next_token=None):

    # multiple runs of this script was used with different twitter api query values to 
    # attempt to capture multiple regions of canada
    # query = "(canada OR british columbia OR vancouver OR toronto OR GTA OR ontario) (covid OR COVID-19 OR coronavirus) business -is:retweet"
    # query = "(alberta OR calgary OR edmonton OR montreal OR quebec OR nova scotia OR newfoundland) (covid OR COVID-19 OR coronavirus) business -is:retweet"
    # query = "(NWT OR yukon OR yellowknife OR whitehorse OR PEI OR gatineau OR victoria) (covid OR COVID-19 OR coronavirus) business -is:retweet"
    query = "(canada OR british columbia OR vancouver OR toronto OR GTA OR ontario) (covid OR COVID-19 OR coronavirus) (business OR economic impact) -is:retweet"

    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id,created_at,entities"
    max_results = "max_results=100"

    if next_token is None:
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}".format(
            query, tweet_fields, max_results
        )
    else:
        next = "next_token={}".format(next_token)
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}&{}".format(
            query, tweet_fields, max_results, next
        )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def connect_to_db():

    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
        secrets.DB_SECRETS["host"], 
        secrets.DB_SECRETS["user"], 
        secrets.DB_SECRETS["dbname"], 
        secrets.DB_SECRETS["password"], 
        secrets.DB_SECRETS["sslmode"]
    )
    conn = psycopg2.connect(conn_string)
    print("Connection established")

    cursor = conn.cursor()

    return {"cursor": cursor, "connection": conn}

def close_db_connection(cursor, conn):
    # Clean up
    conn.commit()
    cursor.close()
    conn.close()

def write_tweets_to_db(connection_original, cursor_original, tweet_json):

    tweets = tweet_json['data']
    meta_data = tweet_json['meta']

    # cursor and connection are reassigned in the scope outside the for loop so changes
    # made in the exception will persist
    connection = connection_original
    cursor = cursor_original

    for i, tweet in enumerate(tweets):
        # Drop previous table of same name if one exists
        # cursor.execute("DROP TABLE IF EXISTS inventory;")
        # print("Finished dropping table (if existed)")

        # Create a table
        # cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
        # print("Finished creating table")

        # Insert tweet into the table
        # all tables have unique contrains such that tweets may only be inserted once on the tweets table and
        # the unique combination of a tweet_id and either an annotation or hashtag may only occur once
        try:
            cursor.execute(
                "INSERT INTO tweets (author_id, tweet_id, text, created_at) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING"
                ,
                (
                    tweet["author_id"], 
                    tweet["id"],
                    tweet["text"],
                    tweet["created_at"]
                )
            )

            if "entities" in tweet:

                if "annotations" in tweet["entities"]:

                    for i, annotation in enumerate(tweet["entities"]["annotations"]):

                        cursor.execute(
                            "INSERT INTO annotations (tweet_id, type, probability, text) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
                            (
                                tweet["id"],
                                annotation["type"],
                                annotation["probability"],
                                annotation["normalized_text"]
                            )
                        )

                if "hashtags" in tweet["entities"]:
                    for i, tag in enumerate(tweet["entities"]["hashtags"]):
                        cursor.execute(
                            "INSERT INTO hashtags (tweet_id, tag) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                            (
                                tweet["id"],
                                tag["tag"]
                            )
                        )
            print("processed tweet: {}".format(tweet["text"]))
        except Exception as e: 
            print("exception error below from tweet_id {}".format(tweet["id"]))
            print(e)

def main():
    
    bearer_token = auth()
    next_token = None

    # set up db connection
    temp = connect_to_db()
    cursor = temp["cursor"]
    connection = temp["connection"]

    # loop to collect 100 tweets, 1000 times
    # we have set an arbitrary limit to collect 100,000 tweets
    for i in range(1000):
        try:

            #if first run fetch tweets, if not fetch next page of tweets
            if next_token is None:
                url = create_url()
            else:
                url = create_url(next_token=next_token)
            
            headers = create_headers(bearer_token)
            json_response = connect_to_endpoint(url, headers)
            # print(json.dumps(json_response, indent=4, sort_keys=True))

            # pass dictionary of tweets to processing function
            write_tweets_to_db(connection, cursor, json_response)

            print("running loop at index {} with next_token={}".format(i, next_token))

            # if there is no next token in the metadata, we have reached the end of the list
            # stop tweet collection here, or if we have collected 100,000 tweets, whichever comes first
            if "next_token" in json_response['meta']:
                next_token = json_response['meta']['next_token']
            else:
                print("exited loop at index {}".format(i))
                break
        except Exception as e:
            print("an error occured at loop index {}:".format(i))
            print(e)
            break
    
    # close db connection after operations
    close_db_connection(cursor, connection)

if __name__ == "__main__":
    main()