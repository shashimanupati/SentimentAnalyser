# Sentiment Analysis for Amazon Fashion Reviews

This script performs sentiment analysis on a dataset of Amazon Fashion reviews using the VADER SentimentIntensityAnalyzer. It calculates the number of positive, negative, and neutral reviews and prints the results.

## Requirements
- Python 3.x
- vaderSentiment package (install using `pip install vaderSentiment`)

## How to Use
1. Ensure you have Python 3.x installed on your system.
2. Install the required `vaderSentiment` package by running `pip install vaderSentiment`.
3. Download the Amazon Fashion reviews dataset from the following link:
   [https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/AMAZON_FASHION.json.gz](https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/AMAZON_FASHION.json.gz)
4. Save the downloaded file as `AMAZON_FASHION.json.gz` in the `data` directory located in the same directory as this script.

## Code Description
The script consists of three main functions:

1. `analyze_sentiment(reviews)`: This function takes a list of reviews as input and uses the VADER SentimentIntensityAnalyzer to calculate the sentiment score for each review's text. It returns a list of sentiment scores.

2. `print_sentiment_analysis(sentiments)`: This function takes a list of sentiment scores as input and prints the sentiment analysis results, showing the count of positive, negative, and neutral reviews.

3. `parse_json(path)`: This is a generator function that reads the gzipped JSON file and yields each line as a Python dictionary.

The script starts by calling the `parse_json` function to read the reviews from the dataset. It then passes the reviews to the `analyze_sentiment` function to obtain the sentiment scores. Finally, the sentiment scores are passed to the `print_sentiment_analysis` function to display the analysis results.

## Note
1. The `vaderSentiment` package is used for sentiment analysis, and it is specifically designed for social media text. It may not be the most accurate choice for all types of textual data.

2. The code processes reviews until it finds 10,000 valid ones or reaches the end of the dataset, whichever comes first. If you wish to analyze more or fewer reviews, you can modify the condition inside the `analyze_sentiment` function.

3. Make sure the JSON data in the dataset follows the expected format with "reviewText" and "summary" keys. If the data structure differs, you may need to modify the code to handle the appropriate keys.

## Disclaimer
This script and the sentiment analysis results may not be 100% accurate as sentiment analysis is a complex task and can vary depending on the data and context. It is essential to interpret the results with caution.

## Attribution
The code uses the VADER SentimentIntensityAnalyzer, developed by Hutto and Gilbert. For more information about VADER, please refer to the following paper:
Hutto, C.J., and Gilbert, E.E. (2014). "VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text." Eighth International Conference on Weblogs and Social Media (ICWSM-14).
