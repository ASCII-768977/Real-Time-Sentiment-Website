import sys
import re
import couchdb
from _pytest import logging
from bs4 import BeautifulSoup
from Historical_Twitter import sentimentAndTime

nums=re.compile('[1-9]+')
pattern1 = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

def get_database(database_name, ip):
    address = 'http://' + 'admin:project@' + ip + ':' + '5984'
    couch = couchdb.Server(address)

    # Check if database exists, create if not
    db_name = database_name
    if db_name in couch:
        logging.info("Database {} already exists.".format(db_name))
        db = couch[db_name]
    else:
        logging.info("Create {} database.".format(db_name))
        db = couch.create(db_name)
    return db

def cleaning_for_sentiment(tweet):
    # Escaping HTML characters
    tweet = BeautifulSoup(tweet).get_text()
    # Removal of hastags/account
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)", " ", tweet).split())
    # Removal of address
    tweet = ' '.join(re.sub("(\w+:\/\/\S+)", " ", tweet).split())
    # remove numbers
    tweet = ' '.join(re.sub(nums, " ", tweet).split())
    return tweet

# def update_db(db):
#     for id in db:
#         tweet = db[id]
#         if 'compound' not in tweet.keys():
#             tweet['text']
#             if tweet['lang'] == 'en':
#                 pred_text = cleaning_for_sentiment(tweet['text'])
#                 sentiment = sentimentAndTime.get_sentiment_scores(pred_text)
#                 time_period = sentimentAndTime.get_period(tweet['created_at'])
#                 tweet['negative'] = sentiment['neg']
#                 tweet['positive'] = sentiment['pos']
#                 tweet['neu']= sentiment['neu']
#                 tweet['compound']= sentiment['compound']
#                 tweet['weekday'] = time_period[0]
#                 tweet['month']=time_period[1]
#                 tweet['day'] = time_period[2]
#                 tweet['hour'] = time_period[3]
#                 tweet['year'] = time_period[4]
#                 #update need update each one, that means update 5 times
#                 db.save(tweet)

if __name__ == '__main__':
    #run on the cluster
    if len(sys.argv) >= 2:
        dbName = sys.argv[1]
        IPaddress = sys.argv[2]
    else:
        print('not enough parameter')
        sys.exit(0)

    #run local
    dbName='south_yarra1'
    IPaddress='45.113.234.34'

    db=get_database(dbName,IPaddress)
    update_db(db)