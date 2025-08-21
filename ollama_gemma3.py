from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

st.title("Yokitha's Chat Bot")
input_txt = st.text_input("Please enter your queries here....")

prompt = ChatPromptTemplate.from_messages(
    [("system","you are a helpful AI assistant."),
     ("user","user query:{query}")])

llm = OllamaLLM(model = "gemma3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_txt:
  st.write(chain.invoke({"query":input_txt}))

