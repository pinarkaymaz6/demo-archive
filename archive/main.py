import numpy as np
import json
from utils import predict_tweet
from flask import Flask, render_template, request


app = Flask(__name__)

with open('theta.npy', 'rb') as f:
    theta = np.load(f)

with open('freqs.npy', 'rb') as f:
    freqs = np.load(f, allow_pickle=True)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/sentiment/logreg')
def sentiment_logreg():
    return render_template('sentiment_logreg.html')


@app.route('/sentiment/logreg/result', methods=['POST'])
def get_sentiment_logreg():
    tweet = json.loads(request.data)
    y_hat = predict_tweet(tweet, freqs.item(), theta)
    confidence = round(float(np.squeeze(y_hat)) * 100, 2)
    sentiment = 'Negative'
    if y_hat > 0.5:
        sentiment = 'Positive'

    result = f"{sentiment} sentiment (confidence: {confidence}%)"
    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
