#import relevant modules
#i chose to not import or utilise spacy after using it lowered the accuracy of sentiment analysis
#import spacy
import pandas as pd
from textblob import TextBlob
import re

#spacy is actually not being used after experimentation
#nlp = spacy.load('en_core_web_sm')
#reading in the data of the reviews
df = pd.read_csv("1429_1.csv")

#looking specifically at text review data
review_data = df["reviews.text"]
#removing any empty text reviews
dropna_data = df.dropna(subset=["reviews.text"])

#function to ensure the review is in lower case with full stops removed
def processed_text(text):
    return (re.sub(r'\s+', ' ',text.lower().replace("."," ")))
    #choice to not remove stop words as many of the stop words such as "not" are actually relevant for sentiment analysis and proved unhelpful
    #tokens_without_stopwords = [token for token in doc if not token.is_stop]
    #return " ".join(token.text for token in tokens_without_stopwords)

#function to get the sentiment of the text review
def get_polarity(review_number):
    cleaned_text = processed_text(dropna_data["reviews.text"].iloc[review_number])
    blob = TextBlob(cleaned_text)
    #analyse the sentiment polarity
    polarity = blob.polarity
    #print the relevant text review, the cleaned data review, the polarity, a predicted review score based on the polarity, and the actual review rating given
    print("The review is: ", dropna_data["reviews.text"].iloc[review_number])
    print("The cleaned review is: ", cleaned_text)
    print("The polarity is: ", polarity)
    print("A predicted review based on sentiment is: ", 3+2*polarity)
    print("The review rating was: ", df["reviews.rating"].iloc[review_number])

#using the function to analyse sentiment of particular reviews
get_polarity(17)
get_polarity(36)
get_polarity(37)
get_polarity(38)
get_polarity(39)