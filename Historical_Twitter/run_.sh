# harvest streaming data
ssh -i /Users/jiaqili/Desktop/id_rsa ubuntu@$2 "chmod 777 StreamSearch.py; nohup python3 StreamSearch.py $1 $2 $3 $4 >/dev/null 2>&1 &"

#harvest tweets by user timeline
ssh -i /Users/jiaqili/Desktop/id_rsa ubuntu@$2 "chmod 777 SearchUser.py; nohup python3 SearchUser.py $1 $2 $3 >/dev/null 2>&1 &"

#process tweets for sentiment analysis
ssh -i /Users/jiaqili/Desktop/id_rsa ubuntu@$2 "chmod 777 process_tweets.py; nohup python3 process_tweets.py $1 $2 >/dev/null 2>&1 &"

#topic modeling for historical data
ssh -i /Users/jiaqili/Desktop/id_rsa ubuntu@$2 "chmod 777 topic_LDA.py; nohup python3 topic_LDA.py $1 $2 $3 >/dev/null 2>&1 &"