import streamlit as st 
import nltk
from textblob import TextBlob
from newspaper import Article

# url = 'https://edition.cnn.com/2020/08/02/tech/microsoft-tiktok/index.html'

"## Enter your News url here"
url = st.text_input("url")

agree = st.checkbox("Submit to summarise the Article")

if agree:
	article = Article(url)

	article.download()
	article.parse()

	article.nlp()

	st.write("Title:")
	article.title

	st.write("Published Date:")
	article.publish_date
	"## **Summary of the News Article**"

	st.write(article.summary)