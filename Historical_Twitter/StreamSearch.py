import time
import threading
import logging
import json
import couchdb
from Historical_Twitter import config
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

def get_database(database_name,ip):
    address = 'http://'+ 'admin:project@' + ip + ':' + '5984'
    couch=couchdb.Server(address)
    # Check if database exists, create if not
    db_name = database_name
    if db_name in couch:
        logging.info("Database {} already exists.".format(db_name))
        db = couch[db_name]
    else:
        logging.info("Create {} database.".format(db_name))
        db = couch.create(db_name)
    return db

class MyListener(StreamListener):
    def __init__(self, db, auth_index):
        self.db= db
        self.auth_index = auth_index

    def get_twitter_auth(self):
        try:
            ckey = config.app_keys_tokens[self.auth_index]['consumer_key']
            csecret = config.app_keys_tokens[self.auth_index]['consumer_secret']
            atoken = config.app_keys_tokens[self.auth_index]['access_token']
            asecret = config.app_keys_tokens[self.auth_index]['access_token_secret']
        except Exception as e:
            print(str(e)+" read_authentication_error")
        
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        return auth

    def on_data(self, data):
        tweet = json.loads(data)
        tweet['_id'] = str(tweet['id'])
        try:
            if tweet['lang']=='en':
                self.db.save(tweet)
        except couchdb.http.ResourceConflict:
            pass
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            # #Returning False on_data method in case rate limit occurs# #
            logging.info(status)
            return False
        else:
            logging.error(str(status) +" auth_index:"+str(self.auth_index))
            return False


class MyThread(threading.Thread):
    def __init__(self, db, region, auth_index):
        threading.Thread.__init__(self)
        self.db = db
        self.region = region
        self.auth_index = auth_index

    def run(self):
        db = get_database(self.db)
        listener = MyListener(db,self.auth_index)
        auth = listener.get_twitter_auth()
        stream = Stream(auth, listener)
        stream.filter(locations=self.region)


if __name__ == "__main__":

    # if len(sys.argv) >= 4:
    #     city_name = sys.argv[1]
    #     geocode = config.coordinates[city_name]
    #     IPaddress = sys.argv[2]
    #     num=sys.argv[3]
    #     index=int(sys.argv[4])
    # else:
    #     print('not enough parameter')
    #     sys.exit(0)
    text=[]
    city_name = 'south_yarra'
    geocode = config.coordinates[city_name]
    IPaddress = '45.113.234.191'
    num='3'
    index=int(0)
    db_name=city_name+num
    print(db_name)
    while True:
        """
        Melbourne = [144.5990, -38.4339, 145.4666, -37.5675] 
        Brisbane = [152.3828, -27.9386, 153.5467, -26.7922] 
        Canberra = [148.9439, -35.5926, 149.3993, -35.1245] 
        Perth = [115.4495, -32.4695, 116.4152, -31.4551] 
        Adelaide = [138.4362, -35.3503, 138.8480, -34.5716] 
        Sydney = [150.2815, -34.1202, 151.3430, -33.5781] 
        
        Calton = [144.956177,-37.80792,144.97608,-37.79226] 
        South_yarra = [144.975788,-37.8481,145.00644,-37.827676] 
        Kew = [144.99927,-37.817374,145.06252,-37.78558]
        Bundoora =[145.0289,-37.72918,145.10364,-37.67647]
        Preston=[144.978979,-37.75571,145.03827,-37.72792]
        CBD=[144.955012,-37.819944,144.974949,-37.80502]
        """
        #16个index 0-15
        db = get_database(db_name,IPaddress)
        listener = MyListener(db, index)
        auth = listener.get_twitter_auth()
        stream = Stream(auth, listener)
        stream.filter(locations=geocode)
   
        # if one twitter token can not be used, this code can use the next twitter token
        logging.info("Wait for 10s")
        time.sleep(10)


