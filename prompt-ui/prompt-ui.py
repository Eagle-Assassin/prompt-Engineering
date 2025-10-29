from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model=ChatOpenAI(model='gpt-4.1',temperature=0,max_completion_tokens=1000)

st.header("Research Tool")
user_input=st.text_input("Enter your promt")

if st.button('Summarize'):
    result =model.invoke(user_input)
    st.write(result.content)