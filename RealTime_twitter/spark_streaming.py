from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.shell import spark
from pyspark.streaming import StreamingContext
from pyspark.ml.feature import CountVectorizer, Tokenizer
from pyspark.ml.clustering import LDA
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
from pyspark.sql import Row, SparkSession
from pyspark.ml.feature import StopWordsRemover, RegexTokenizer, CountVectorizer
import requests
import couchdb

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
_analyzer = SentimentIntensityAnalyzer()

def topic_modelling(time, rdd):
    if not rdd.isEmpty():
        print(time)
        sentences = rdd.zipWithIndex()
        sentences_df = spark.createDataFrame(sentences, ['sentence', 'id'])
        sentences_df.show()

        # tokenize sentences
        print('tokens')
        tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
        regexTokenizer = RegexTokenizer(inputCol="sentence", outputCol="words", pattern="\\W")
        countTokens = udf(lambda words: len(words), IntegerType())
        tokenized = regexTokenizer.transform(sentences_df)
        tokenized.select("sentence", "words").show(truncate=True)

        # remove stop words
        locale = sc._jvm.java.util.Locale
        locale.setDefault(locale.forLanguageTag("en-US"))
        remover = StopWordsRemover(inputCol="words", outputCol="filtered")
        st_flitered = remover.transform(tokenized)
        st_flitered.select("words", "filtered").show(truncate=False)

        # fit to feature model
        cv = CountVectorizer(inputCol="filtered", outputCol="features", vocabSize=5)
        cv_model = cv.fit(st_flitered)
        result = cv_model.transform(st_flitered)
        result.select('filtered', 'features').show()

        # load topic modeling-LDA
        topic = 5
        lda = LDA(k=topic, maxIter=100, optimizer='online')
        lda_model = lda.fit(result)

        topics = lda_model.describeTopics(maxTermsPerTopic=10)
        vocabArray = cv_model.vocabulary
        ListOfIndexToWords = udf(lambda wl: list([vocabArray[w] for w in wl]))
        FormatNumbers = udf(lambda nl: ["{:1.4f}".format(x) for x in nl])
        print("The topics described by their top-weighted terms:")
        topics.select(ListOfIndexToWords(topics.termIndices).alias('words')).show()
        #         topics.select(FormatNumbers(topics.termWeights).alias('features')).show()
        hot_topics= topics.select(ListOfIndexToWords(topics.termIndices).alias('words'))
        #         send2web(hot_topics, sentences_df)
        save2db(hot_topics, sentences_df)
        sent2web(hot_topics, sentences_df)

def get_sentiment_scores(s):
    analysised = _analyzer.polarity_scores(s)
    return analysised['compound']

def save2db(topic_df, sentiment_df):
    IPaddress = "45.113.234.105"
    address = 'http://admin:project@' + IPaddress + ':5984/'
    couch = couchdb.Server(address)
    name = 'real_mel_cluster'

    try:
        db = couch[name]
    except Exception:
        db = couch.create(name)

    top = [t.words for t in topic_df.collect()]
    hotTopics = []
    for i in range(len(top)):
        s = "".join(top[i].split('['))
        s = "".join(s.split(']'))
        s = "".join(s.split(','))
        hotTopics.append(s)
    print("hot topic is", hotTopics)

    # process sentiment_df
    sentences_list = sentiment_df.select('sentence').collect()
    sentiments = []
    for i in sentences_list:
        try:
            score = get_sentiment_scores(i.sentence)
        except:
            continue
        sentiments.append(score)
    period_total = 0.0
    for i in sentiments:
        period_total += i
    leng = 0
    if len(sentiments) == 0:
        leng = 1
    else:
        leng = len(sentiments)
    avgSentiment = period_total / leng
    print(avgSentiment)
    new_dict = {
        "avgSentiment": avgSentiment,
        "hotTopics": hotTopics
    }
    db.save(new_dict)


def sent2web(topic_df, sentiment_df):
    # process topic_df
    top = [t.words for t in topic_df.collect()]
    print(top)
    hotTopics = []
    for i in range(len(top)):
        s = "".join(top[i].split('['))
        s = "".join(s.split(']'))
        s = "".join(s.split(','))
        hotTopics.append(s)
    print("hot topic is", hotTopics)

    # process sentiment_df
    sentences_list = sentiment_df.select('sentence').collect()
    sentiments = []
    for i in sentences_list:
        try:
            score = get_sentiment_scores(i.sentence)
        except:
            continue
        sentiments.append(score)
    period_total = 0.0
    for i in sentiments:
        period_total += i
    if len(sentiments) == 0:
        leng = 1
    else:
        leng = len(sentiments)
    avgSentiment = period_total / leng
    print(avgSentiment)

    # according to web url sent to frondend
    urlMel = 'http://45.113.234.34:80/updateMel'
    # some problems
    request_mel = {'hotTopics': str(hotTopics), 'avgSentiment': str(avgSentiment)}
    response1 = requests.post(urlMel, data=request_mel)

if __name__ == "__main__":
    sc = SparkContext.getOrCreate()
    # Create a local StreamingContext with two working thread and batch interval of 20 second
    ssc = StreamingContext(sc, 30)
    lines = ssc.socketTextStream("45.113.234.207", 7004).window(3000)
    words = lines.flatMap(lambda line: line.split("\n"))
    words.foreachRDD(topic_modelling)
    ssc.start()  # Start the computation
    ssc.awaitTermination()

