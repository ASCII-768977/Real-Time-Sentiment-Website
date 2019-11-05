from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import sys
import couchdb
import Pres4topic
import json

def get_topic(text):
    try:
        print('start tf_vectorizer')
        #use tf-idf to vectorizer files
        vectorizer = TfidfVectorizer()
        tf = vectorizer.fit_transform(text)
        numOfTopics=5
        print('start lda')
        lda_model = LatentDirichletAllocation(n_components=numOfTopics, max_iter=50,
                                        learning_method='online',
                                        learning_offset=50.,
                                        random_state=0)
        lda_model.fit(tf)
        def print_top_words(model, feature_names, n_top_words):
            temp = {}
            for topic_idx, topic in enumerate(model.components_):
                key = "Hot Topic %d:" % topic_idx
                value = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
                temp[key] = value
            return temp

        n_top_words = 10
        tf_feature_names = vectorizer.get_feature_names()
        #return 10 topics
        return print_top_words(lda_model, tf_feature_names, n_top_words)
    except:
        print('Something is wrong, but CANNOT help, sorry')

def read_data(ip,name):
    # ip = '45.113.234.191'
    address = 'http://admin:project@' + ip + ':5984/'
    couch = couchdb.Server(address)
    # name = 'adelaide1'
    db = couch[name]
    text=[]
    for id in db:
        tweet = db[id]
        if tweet['year']=='2019':
            pred=Pres4topic.preprocess_sents(tweet['text'])
            text.append(pred)
    print(len(text))
    return text

if __name__=='__main__':
    text=[]
    with open('/Users/jiaqili/Desktop/project/text_view19 syd.json','r') as f:
        line=f.readline()
        while line:
            l = line.strip('\n, ')
            if l.startswith('{') and l.endswith('}'):
                l = json.loads(l)
                tweet = l['value']
                # print(tweet)
                text.append(tweet)
            line = f.readline()
    #use the ubuntu run
    # if len(sys.argv) >= 2:
    #     city_name = sys.argv[1]
    #     IPaddress = sys.argv[2]
    # else:
    #     print('not enough parameter')
    #     sys.exit(0)
    #connect to db
    #local test
    IPaddress='45.113.234.191'
    city_name='sydney'
    address='http://admin:project@' + IPaddress + ':5984/'
    couch = couchdb.Server(address)
    name='topics'
    try:
        db=couch[name]
    except:
        db = couch.create(name)
    #db format {location:year:hot_topics}
    print('start')
    dict=get_topic(text)
    dict['location']=city_name
    print(dict)
    db.save(dict)
    print('done')