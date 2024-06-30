# Query Assistant Application using OpenAI Language Model

# Import necessary modules
import os
import streamlit as st
#from sql_execution import execute_sf_query
from langchain import OpenAI
from langchain.prompts import load_prompt
from pathlib import Path
#from PIL import Image
#from app_secrets import OPENAI_API_KEY

#setup env variable
#os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
#project root directory
current_dir = Path(__file__)
root_dir = [p for p in current_dir.parents if p.parts[-1]=='text_to_sql_proj'][0]

#Create Streamlit frontend
st.set_page_config(
    page_title="AI Based SQL Query Assistant"
)
st.sidebar.success("Select a page above")

tab_titles=[
    "Results",
    "Query"
]
st.title("Your AI Based SQL Query Assistant")
prompt = st.text_input("enter your question")
tabs = st.tabs(tab_titles)
