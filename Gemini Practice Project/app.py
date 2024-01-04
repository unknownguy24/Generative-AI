from dotenv import load_dotenv
load_dotenv()  # will load all the environment variables

import streamlit as st
import os
import google.generativeai as genai 

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini model
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#Initializing our streamlit app

st.set_page_config(page_title="Question and Answer Demo")

st.header("Sid's Gemini Application")

input = st.text_input("Input: ", key = "input")

submit = st.button("Submit the question")

#Submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("Answer is ")
    st.write(response)

