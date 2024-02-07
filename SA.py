import streamlit as st
from altair import Chart
from textblob import TextBlob
from requests import post
import nltk

def sentiment(input):
    blob = TextBlob(input)
    sentiment = blob.sentiment.polarity #-1 to 1
    # print(sentiment)
    # print(input)
    return sentiment


def main():
    st.title("GURU PRASAATH NEW APP")
    st.header("Enter the text")
    user_input = st.text_input("")
    output = sentiment(user_input)
    st.write("Your Sentiment analysis is....")
    st.write(output)

if __name__ == "__main__":
    main()