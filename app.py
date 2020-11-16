import streamlit as st 
from newspaper import Article
nltk.download("punkt")

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
