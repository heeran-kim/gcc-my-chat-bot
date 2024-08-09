"""
This simple chatbot application allows users to upload a PDF file and extracts the text content from it,
and then splits the text into manageable chunks. The extracted text is then displayed on the web page
Users can input questions to perform similarity searches on the text. (NEW)
The app returns the most relevant text chunks based on the user's query, enabling a basic chatbot functionality. (NEW)

Libraries used:
- Streamlit: For creating the web interface.
- PyPDF2: For reading and extracting text from PDF files.
- LangChain: For splitting text into chunks.
- OpenAIEmbeddings: For generating embeddings from text chunks.
- FAISS: For storing embeddings in a vector store.

Features:
- PDF File Upload: Users can upload a PDF file via the sidebar.
- Text Extraction: The app extracts text from each page of the PDF and displays it.
- User Prompt: If no file is uploaded, the app prompts the user to upload a file.
- Text Splitting: The extracted text is split into chunks using the RecursiveCharacterTextSplitter from LangChain.
    This is useful for processing large texts in smaller parts.
- Embeddings Generation: The text chunks are converted into embeddings using OpenAI's API.
- Vector Store: The embeddings are stored in a FAISS vector store for efficient similarity search.
- User Query Input: Allows the user to input a question, which is then matched against the text chunks to find relevant information. (NEW)
- Similarity Search: The app performs a similarity search using FAISS and returns the most relevant text chunks based on the user's question. (NEW)

Output:
- The extracted text chunks are displayed on the web page.
- The results of the similarity search are displayed based on the user's query. (NEW)


This application can be a foundational step for building more complex text processing or chatbot applications based on PDF content.
"""
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import os

key = os.getenv("OPEN_API_KEY")

st.header("A simple chat bot based on one pdf file")

st.sidebar.header("Document")

file = st.sidebar.file_uploader("Input a PDF file", type='pdf')

text_splitter = RecursiveCharacterTextSplitter(
    separators = "\n",
    chunk_size = 1000,
    chunk_overlap = 150,
    length_function = len
)

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    chunks = text_splitter.split_text(text)
    st.write(chunks)
    embeddings = OpenAIEmbeddings(openai_api_key = key)
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Input field for user questions
    question = st.text_input("Input your question")
    # Perform similarity search with the user's question
    matches = vector_store.similarity_search(question)
    if question:
        st.write(matches)
else:
    st.write("Input a file...")
