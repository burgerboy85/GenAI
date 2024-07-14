# Query Assistant Application using OpenAI Language Model

# Import necessary modules
import os
import streamlit as st
from mysql_conn import execute_ms_query
from langchain import OpenAI, LLMChain
from langchain.prompts import load_prompt
from pathlib import Path
#from PIL import Image
from app_secrets import OPENAI_API_KEY

#setup env variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
#project root directory
current_dir = Path(__file__)
#root_loc = [p for p in current_dir.parents if p.parts[-1]=='text_to_sql_proj'][0]
root_loc = [p for p in current_dir.parents if p.parts[-1]=='my_project'][0]
print(root_loc)


#Create Streamlit frontend
st.set_page_config(
    page_title="AI Based SQL Query Assistant"
)
#st.sidebar.success("Select a page above")

tab_titles=[
    "Results",
    "Query"
]
st.title("Your AI Based SQL Query Assistant")
user_input = st.text_input("enter your question")
tabs = st.tabs(tab_titles)

#Create the Prompt
#t2s_prompt_template = load_prompt(f'{root_loc}/prompts/prompt.yaml')
t2s_prompt_template = load_prompt(f'{root_loc}/metadata/test.yaml')

#Create the LLM
t2s_llm = OpenAI(temperature=0) 
t2s_generation_chain = LLMChain(llm=t2s_llm,prompt=t2s_prompt_template,verbose=True)

if user_input:
    t2s_sql_query = t2s_generation_chain(user_input)
    t2s_result = execute_ms_query(t2s_sql_query['text'])
#Show the result in Streamlit
    with tabs[0]:
        st.write(t2s_result)
    with tabs[1]:
        st.write(t2s_sql_query['text'])        
 