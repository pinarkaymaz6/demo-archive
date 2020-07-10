import numpy as np
import json
from utils import predict_tweet, naive_bayes_predict
from flask import Flask, render_template, request


app = Flask(__name__)

with open('freqs.npy', 'rb') as f:
    freqs = np.load(f, allow_pickle=True)

with open('theta.npy', 'rb') as f:
    theta = np.load(f)


with open('loglikelihood.npy', 'rb') as f:
    loglikelihood = np.load(f, allow_pickle=True)



#Home

@app.route('/')
def root():
    return render_template('index.html')


#Sentiment Analysis with Logistic Regression

@app.route('/sentiment/logreg')
def sentiment_logreg():
    return render_template('sentiment_logreg.html')


@app.route('/sentiment/logreg/result', methods=['POST'])
def get_sentiment_logreg():
    tweet = json.loads(request.data)
    y_hat = predict_tweet(tweet, freqs.item(), theta)
    score = round(float(np.squeeze(y_hat)), 4)
    sentiment = 'Negative'
    if y_hat > 0.5:
        sentiment = 'Positive'

    result = f"{sentiment} sentiment (Score: {score})"
    return result

# Sentiment Analysis with Naive Bayes

@app.route('/sentiment/naivebayes')
def sentiment_naive_bayes():
    return render_template('sentiment_naive_bayes.html')


@app.route('/sentiment/naivebayes/result', methods=['POST'])
def get_sentiment_naive_bayes():
    tweet = json.loads(request.data)
    p = naive_bayes_predict(tweet, 0, loglikelihood.item())
    sentiment = "Positive" if p>=0 else "Negative"
    result = f"{sentiment} sentiment (Score: {round(p, 4)})"
    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
