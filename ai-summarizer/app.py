import streamlit as st
import nltk
from textblob import TextBlob
from newspaper import Article

# Download punkt if not already installed
nltk.download('punkt')
nltk.download('punkt_tab')

st.set_page_config(page_title="News Summarizer", layout="wide")

st.title("📰 News Summarizer")

url = st.text_input("Enter Article URL")

if st.button("Summarize"):

    if url.strip() == "":
        st.warning("Please enter a valid URL.")
    else:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()

            # Display results
            st.subheader("Title")
            st.write(article.title)

            st.subheader("Author(s)")
            st.write(", ".join(article.authors) if article.authors else "Not Available")

            st.subheader("Publishing Date")
            st.write(article.publish_date if article.publish_date else "Not Available")

            st.subheader("Summary")
            st.write(article.summary)

            # Sentiment Analysis
            analysis = TextBlob(article.text)
            polarity = analysis.polarity

            if polarity > 0:
                sentiment_label = "Positive 😊"
            elif polarity < 0:
                sentiment_label = "Negative 😠"
            else:
                sentiment_label = "Neutral 😐"

            st.subheader("Sentiment Analysis")
            st.write(f"Polarity: {polarity}")
            st.write(f"Sentiment: {sentiment_label}")

        except Exception as e:
            st.error(f"Error: {e}")
