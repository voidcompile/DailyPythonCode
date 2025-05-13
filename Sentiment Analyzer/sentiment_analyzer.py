from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Get the sentiment polarity
    polarity = blob.sentiment.polarity

    # Determine the sentiment
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity

def main():
    print("Welcome to Sentiment Analyzer!")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        text = input("Enter a text to analyze sentiment: ")
        
        if text.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        sentiment, polarity = analyze_sentiment(text)
        
        # Print sentiment and polarity
        print(f"Sentiment: {sentiment}")
        print(f"Polarity: {polarity}\n")
        
        # Daily reminder message
        print("Don't forget to stay positive and keep learning! Keep going! 💪")

if __name__ == "__main__":
    main()
