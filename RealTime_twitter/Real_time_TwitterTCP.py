import socket
import requests
import requests_oauthlib
import json
import sys

from RealTime_twitter.Preprocessing import cleaning
from RealTime_twitter.config import coordinates_str
from RealTime_twitter import config


# au cities: melbourne, sydney, adleide, brisbane
# melbourne subs: south_yarra, cbd,

def get_tweets(my_auth, city_name):
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'), ('locations', coordinates_str[city_name])]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response)
    return response

def send_tweets_to_spark(http_resp, tcp_connection):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']

            # pre_processing tweet
            tweet_clean = cleaning(tweet_text)
            print("Tweet Text: " + tweet_clean)
            print("-------------------- ----------------------")
            tcp_connection.send((tweet_clean + '\n').encode())
        except:
            pass

if __name__ == "__main__":
    #system run
    if len(sys.argv) >= 2:
        city_name = sys.argv[1]
        IPaddress = sys.argv[2]
        auth_index= int(sys.argv[3])
        TCP_PORT =int(sys.argv[4])
    else:
        print('not enough parameter')
        sys.exit(0)

    #local test
    # city_name = 'melbourne'
    # IPaddress = 'localhost'
    # auth_index = 0
    #TCP_PORT = 7003

    #authorization
    consumer_key = config.app_keys_tokens[auth_index]['consumer_key']
    consumer_secret = config.app_keys_tokens[auth_index]['consumer_secret']
    access_token = config.app_keys_tokens[auth_index]['access_token']
    access_secret = config.app_keys_tokens[auth_index]['access_token_secret']
    my_auth = requests_oauthlib.OAuth1(consumer_key, consumer_secret, access_token, access_secret)

    while True:
        TCP_IP = IPaddress
        conn = None
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(3)
        print("Waiting for TCP connection...")
        conn, addr = s.accept()
        print("Connected... Starting getting tweets.")
        resp = get_tweets(my_auth, city_name)
        send_tweets_to_spark(resp, conn)
