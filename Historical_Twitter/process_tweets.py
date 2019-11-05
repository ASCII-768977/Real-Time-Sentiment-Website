import couchdb
from Historical_Twitter.sentimentAndTime import get_sentiment_scores, get_period
from Historical_Twitter import pre4sen
import logging


def get_database(db_name, ip):
    address = 'http://' + 'admin:project@' + ip + ':' + '5984'
    couch = couchdb.Server(address)
    print(db_name)
    # Check if database exists, create if not

    if db_name in couch:
        logging.info("Database {} already exists.".format(db_name))
        db = couch[db_name]
    else:
        logging.info("Create {} database.".format(db_name))
        db = couch.create(db_name)
    return db


def processing_db(db):
    for id in db:
        tweet = db[id]
        if 'compound' not in tweet.keys():
            tweet['text']
            if tweet['lang'] == 'en':
                time_period = get_period(tweet['created_at'])
                pred_text = pre4sen.cleaning_for_sentiment(tweet['text'])
                sentiment = get_sentiment_scores(pred_text)
                tweet['text'] = pred_text
                tweet['negative'] = sentiment['neg']
                tweet['positive'] = sentiment['pos']
                tweet['neu'] = sentiment['neu']
                tweet['compound'] = sentiment['compound']
                tweet['weekday'] = time_period[0]
                tweet['month'] = time_period[1]
                tweet['day'] = time_period[2]
                tweet['hour'] = time_period[3]
                tweet['year'] = time_period[4]
                db.save(tweet)
            else:
                db.delete(tweet)


if __name__ == '__main__':
    # run on cluster
    # if len(sys.argv) >= 2:
    #     city_name = sys.argv[1]
    #     IPaddress = sys.argv[2]
    # else:
    #     print('not enough parameter')
    #     sys.exit(0)

    print('start')
    # run local
    city_name = 'south_yarra3'
    IPaddress = '45.113.234.34'

    db = get_database(city_name, IPaddress)
    processing_db(db)
    print('done')

