from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import sys
import couchdb
import logging
from Historical_Twitter import Pre4Topic

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

def read_data(city_name,ip,month):
    text=[]
    db=get_database(city_name,ip)
    dv = db.view('_design/textview/_view/time-view19-'+month)
    for row in dv:
        print(row)
        t=Pre4Topic.cleaning_for_topic(row.value)
        text.append(t)
    return text


if __name__=='__main__':
    #run on cluster
    # if len(sys.argv) >= 2:
    #     city_name = sys.argv[1]
    #     IPaddress = sys.argv[2]
    #     month=sys.argv[3]
    # else:
    #     print('not enough parameter')
    #     sys.exit(0)

    #local test
    city_name='sydney1'
    IPaddress = '45.113.234.191'
    month='Jan'

    print('start')
    text=read_data(city_name,IPaddress,month)

    name = 'topics'
    db=get_database(name,IPaddress)
    dict=get_topic(text)
    dict['location']=city_name
    dict['month']= month
    print(dict)
    db.save(dict)
    print('done')