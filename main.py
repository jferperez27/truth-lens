from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_score(sentence : str) -> None:
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print(f"Sentiment Scores: {sentiment_dict}")
    print(f"Negative Sentiment: {sentiment_dict['neg']*100}%")
    print(f"Neutral Sentiment: {sentiment_dict['neu']*100}%")
    print(f"Positive Sentiment: {sentiment_dict['pos']*100}%")
    
    print("\n\nResults...\n\n")

    if sentiment_dict['compound'] >= 0.05:
        print("Overall Sentiment: Positive")
    elif sentiment_dict['compound'] <= -0.05:
        print("Overall Sentiment: Negative")
    else:
        print("Overall Sentiment: Neutral")


if __name__ == "__main__":
    while True:
        user_sentence = input()
        print("\nChecking Sentiment... \n")
        sentiment_score(user_sentence)
        print("\n")