import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

def initialize_llama_model(api_key):    
    llm = ChatGroq(
        groq_api_key=api_key,
        model='llama3-8b-8192'
    )
    if llm is None:
        raise Exception("Llama model initialization failed.")
    return llm

