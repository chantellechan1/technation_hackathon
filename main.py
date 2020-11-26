import requests
import os
import json
import secrets

# ---------- old code -------------------
# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


# def auth():
#     return os.environ.get("BEARER_TOKEN")
# ---------- end old code ----------------

# A Twitter API bearer token is required to run this script, it is expected
# that the bearer token is stored in secrets.py in the same directory, and
# is set as follows:
# BEARER_TOKEN = <your bearer token>

def auth():
    return secrets.BEARER_TOKEN

def create_url(next_token=None):
    # TODO: add next_token functionality to get multiple pages of results
    # IDEA: if number of results less than max results, stop looping for results

    query = "(canada OR british columbia OR vancouver OR toronto OR GTA OR ontario) (covid OR COVID-19 OR coronavirus) business -is:retweet"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id,created_at,entities"
    max_results = "max_results=11"

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

def process_tweets(tweet_json):
    tweets = tweet_json['data']
    meta_data = tweet_json['meta']

    for i, tweet in enumerate(tweets):
        print("{}: {}".format(i, tweet['text']))
    
    # TODO: do something to process these tweets and upload them to be saved somewhere


def main():
    bearer_token = auth()
    next_token = None
    tweet_list = []

    for i in range(2):
        print('run #{}'.format(i))

        if next_token is None:
            url = create_url()
        else:
            url = create_url(next_token=next_token)
        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(url, headers)
        # print(json.dumps(json_response, indent=4, sort_keys=True))

        # pass dictionary of tweets to processing function
        process_tweets(json_response)
        next_token = json_response['meta']['next_token']

if __name__ == "__main__":
    main()