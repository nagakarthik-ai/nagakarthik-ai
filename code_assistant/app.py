import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-4o",
    temperature=0.5
)

# Define the prompt
prompt = PromptTemplate(
    input_variables=["code_task"],
    template="""
You are a professional coding assistant. Help the user with the following task:
{code_task}
Provide clean, well-commented code and explanations if needed.
"""
)
