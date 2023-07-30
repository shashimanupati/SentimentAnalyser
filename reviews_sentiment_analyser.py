import gzip, json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(reviews):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    count = 0
    for review in reviews:
        if "reviewText" in review:
            review_text = review["reviewText"]
        
        if review_text is None and "summary" in review:
            summary = review["summary"]

        if review_text is not None:
            sentiment_score = analyzer.polarity_scores(review_text)
        if sentiment_score is None and summary is not None:
            sentiment_score = analyzer.polarity_scores(summary)

        if sentiment_score is None:
            print("no info found for this review")
        else:
            sentiments.append(sentiment_score)
            count = count + 1

        if count > 10000:
            return sentiments
    return sentiments

def print_sentiment_analysis(sentiments):
    positive_count = sum(1 for sentiment in sentiments if sentiment['compound'] >= 0)
    negative_count = sum(1 for sentiment in sentiments if sentiment['compound'] < 0)
    neutral_count = len(sentiments) - (positive_count + negative_count)

    print("Sentiment Analysis Results:")
    print(f"Positive reviews: {positive_count}")
    print(f"Negative reviews: {negative_count}")
    print(f"Neutral reviews: {neutral_count}")

def parse_json(path):
  g = gzip.open(path, 'r')
  for l in g:
    l_str = l.decode('utf-8')
    yield json.loads(l_str)

if __name__ == "__main__":
    reviews = parse_json('data\AMAZON_FASHION.json.gz')

    if not reviews:
        print("no reviews found")
    else:
        sentiments = analyze_sentiment(reviews)
        print_sentiment_analysis(sentiments)
