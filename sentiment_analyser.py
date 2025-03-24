from textblob import TextBlob  # Importing TextBlob for sentiment analysis

def analyze_audience_sentiment(blog):
    """
    Analyzes the sentiment of a given blog post.

    Args:
        blog (str): The blog content to analyze.

    Returns:
        str: Sentiment classification - 'Positive', 'Negative', or 'Neutral'.
    """
    sentiment_score = TextBlob(blog).sentiment.polarity  # Calculate sentiment polarity
    
    # Determine sentiment based on polarity score
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"
