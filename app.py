import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Read the README.md file
def load_readme():
    try:
        with open("README.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""


# Configure the Generative AI model
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the GEMINI_API_KEY in your .env file.")
    st.stop()  # Stop execution if API key is not found


genai.configure(api_key=api_key)
gemini = genai.GenerativeModel(model_name="gemini-pro")

# App title and description
st.title("Secure API Key Handling Demonstration")
st.write(
    "This app demonstrates how to securely manage API keys using environment variables."
)
# Optionally, provide a button to display the README
with st.expander("README MORE", expanded=False):
    st.markdown(load_readme())

# User input for prompt
prompt = st.text_input(
    "Ask a Question:", value="What are best practices for using environment variables?"
)

# Generate and display response if prompt is provided
if prompt:
    response = gemini.generate_content(prompt)
    st.subheader("Gemini Response:")
    st.write(response.text)
