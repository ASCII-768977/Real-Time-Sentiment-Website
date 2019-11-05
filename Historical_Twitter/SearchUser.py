from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import logging
from Historical_Twitter import config
import couchdb
from couchdb import design
import time
from Historical_Twitter.config import coordinates
# create a view of raw db so that the precessed twitter will not be shown in this view again
# which can prevent one twitter from been processed many times
# 这个view function

city_list=['south_yarra','calton','kew','bundoora','preston','cbd','clayton','doncaster','camberwell','brighton']


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

def get_area(coordinate):
	#coordinate[0]=longtitude
	#coordinate[1]=latitude
	name=' '
	for key, value in coordinates.items():
		if coordinate[0]<=value[3] and coordinate[0]>=value[1] and coordinate[1]<=value[2] and coordinate[1]>=value[0]:
			name = key
	return name

def view_unprocessed_raw(db):
    map_fnc = '''function(doc) {
        if (!doc.username) {
            emit(doc._id, null);
        }
    }'''
    view = design.ViewDefinition('original_tweets', 'username_not_used', map_fnc)
    view.sync(db)

# api.friends and api.user_timeline in search API
def get_user_timeline_tweets(db, api,city_name):
    result = db.view('original_tweets/username_not_used')
    for res in result:
        print(res)
        id = res['id']
        tweet = db[id]
        name = tweet['user']['screen_name']
        print('屏幕上的名字',name)
        print('地区名字',city_name)
        try:
            for raw_tweet in Cursor(api.user_timeline, screen_name=name).items(100):
                print('生的数据先出来',raw_tweet._json)
                raw_tweet._json['_id'] = str(raw_tweet._json['id'])
                raw_tweet._json['username'] = True
                print('有地址么',raw_tweet._json['place']['name'])
                # area_name = raw_tweet._json['place']['name']
                # print('地区名字',area_name)
                # if raw_tweet._json['geo']!='null':
                #     city_name=get_area(raw_tweet._json['geo']['coordinate'])
                #     print(city_name)
                # print('地区名字变了么',city_name)
                # print(area_name)
                # if city_name in city_list:
                #     city_name='melbourne'
                #     print(city_name)
                try:
                    print('难道没有语言？？',raw_tweet._json['lang'])
                    if raw_tweet._json['lang'] == 'en':
                        print('这是存进去的',raw_tweet)
                        db.save(raw_tweet)
                except couchdb.http.ResourceConflict:
                    print('ignor duplicate')
                    pass
            doc = db.get(id)
            doc['username'] = True
            db.save(doc)
        except:
            pass

if __name__ == '__main__':
    #sleep 20s for getting streaming data
    logging.info("wait for 20s")
    time.sleep(20)

    # run on cluster
    # if len(sys.argv) >= 2:
    #     city_name = sys.argv[1]
    #     IPaddress = sys.argv[2]
    #     auth_index= int(sys.argv[3])
    # else:
    #     print('not enough parameter')
    #     sys.exit(0)

    #run local
    city_name = 'south_yarra'
    IPaddress = '45.113.234.105'
    auth_index = 17

    city1=['sydney','adelaide', 'south_yarra', 'calton']
    city2=['melbourne', 'brisbane', 'kew', 'bundoora']
    city3=['perth', 'canberra', 'clayton', 'camberwell']
    city4=['cbd', 'doncaster', 'preston', 'brighton']

    if city_name in city1:
        num = '1'
    if city_name in city2:
        num = '2'
    if city_name in city3:
        num = '3'
    if city_name in city4:
        num = '4'

    #authorised the tweets accounts
    consumer_key= config.app_keys_tokens[auth_index]['consumer_key']
    consumer_secret = config.app_keys_tokens[auth_index]['consumer_secret']
    access_token = config.app_keys_tokens[auth_index]['access_token']
    access_secret = config.app_keys_tokens[auth_index]['access_token_secret']

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = API(auth, wait_on_rate_limit=True)

    db=get_database(city_name+'3',IPaddress)

    while True:
        logging.info("Start get tweet by username")
        view_unprocessed_raw(db)
        print('something')
        get_user_timeline_tweets(db, api,city_name)
        print('is it start?')
        logging.info("No new tweets, wait for 60 seconds")
        time.sleep(60)

