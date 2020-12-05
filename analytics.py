import requests
import os
import json
import secrets
import psycopg2
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import statistics
from collections import Counter

def azure_authenticate_client():
    ta_credential = AzureKeyCredential(secrets.AZURE_SERCRETS['key'])
    text_analytics_client = TextAnalyticsClient(
        endpoint=secrets.AZURE_SERCRETS['endpoint'],
        credential=ta_credential,
        api_version="TextAnalyticsApiVersion.V3_0")
    print("authenticated with azure")
    return text_analytics_client


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
    print("Postgresql db onnection established")

    cursor = conn.cursor()

    return {"cursor": cursor, "connection": conn}


def close_db_connection(cursor, conn):
    # Clean up
    conn.commit()
    cursor.close()
    conn.close()

def push_analytics_to_db(analytics):

    # ran out of time to implement this functionality
    # for now, save to local file
    with open('analytics.json', 'w') as data_file:
        json.dump(analytics, data_file)

def fetch_tweets(index, max_tweets, cursor):
    # index supplied will be used to return tweets greater that the given index (used as id)
    cursor.execute("""
        SELECT * FROM public.tweets
        WHERE id > 0
        ORDER BY id ASC
        LIMIT 10;
    """)

    tweet_data = cursor.fetchall()

    tweets = []
    for tweet in tweet_data:
        tweets.append({
            "id": tweet[0],
            "author_id": tweet[1],
            "tweet_id": tweet[2],
            "text": tweet[3],
            "created_at": tweet[4],
        })
    
    return tweets

def all_tweets_avg_sentiment(cursor, az_client):
    print('begin sentiment analysis')
    
    sentiments = {
        "positive": [],
        "neutral": [],
        "negative": []
    }
    
    for i in range(100):
        print('processing: {}%'.format(i))
        db_index = 3993+i*10
        tweets = fetch_tweets(db_index, 10, cursor)

        documents = []

        for tweet in tweets:
            documents.append(tweet['text'])

        analysis_results = az_client.analyze_sentiment(documents = documents)

        for res in analysis_results:
            sentiments['positive'].append(round(res.confidence_scores.positive, 2)),
            sentiments['neutral'].append(round(res.confidence_scores.neutral, 2)),
            sentiments['negative'].append(round(res.confidence_scores.negative, 2))
    
    pos_avg = sum(sentiments['positive'])/len(sentiments['positive'])
    print("average canadian postive: {}".format(pos_avg))

    neutral_avg = sum(sentiments['neutral'])/len(sentiments['neutral'])
    print("average canadian neutral: {}".format(neutral_avg))

    print("average canadian negative: {}".format(sum(sentiments['negative'])/len(sentiments['negative'])))

    print("Postive mode: {}".format(Counter(sentiments['positive']).most_common(2)))
    print("Neutral mode: {}".format(Counter(sentiments['neutral']).most_common(2)))
    print("Negative mode: {}".format(Counter(sentiments['negative']).most_common(2)))

    return {
        "sentiments": sentiments,
        "averages": {
            "positive": sum(sentiments['positive'])/len(sentiments['positive']),
            "neutral": sum(sentiments['neutral'])/len(sentiments['neutral']),
            "negative": sum(sentiments['negative'])/len(sentiments['negative'])
        }
    }

def main():
    # set up db connection
    temp = connect_to_db()
    cursor = temp["cursor"]
    connection = temp["connection"]

    # set up azure connection
    az_client = azure_authenticate_client()

    analtyics = all_tweets_avg_sentiment(cursor, az_client)

    # add analysis to db
    push_analytics_to_db(analtyics)

    # clean up
    close_db_connection(cursor, connection)


if __name__ == "__main__":
    main()
