import streamlit as st

# tag::llm[]
# Create the LLM
from langchain_ollama.chat_models import ChatOllama

llm = ChatOllama(model="llama3.1", base_url="http://host.docker.internal:11434")
# end::llm[]

# tag::embedding[]
# Create the Embedding model
from langchain_ollama.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3.1")
# end::embedding[]
