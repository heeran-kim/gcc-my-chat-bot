"""
This simple chatbot application allows users to upload a PDF file and extracts the text content from it,
and then splits the text into manageable chunks. (NEW)
The extracted text is then displayed on the web page.

Libraries used:
- Streamlit: For creating the web interface.
- PyPDF2: For reading and extracting text from PDF files.
- LangChain: For splitting text into chunks. (NEW)

Features:
- PDF File Upload: Users can upload a PDF file via the sidebar.
- Text Extraction: The app extracts text from each page of the PDF and displays it.
- User Prompt: If no file is uploaded, the app prompts the user to upload a file.
- Text Splitting: The extracted text is split into chunks using the RecursiveCharacterTextSplitter from LangChain.
    This is useful for processing large texts in smaller parts. (NEW)

Output:
- The extracted text chunks are displayed on the web page. (NEW)

This application can be a foundational step for building more complex text processing or chatbot applications based on PDF content.
"""
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.header("A simple chat bot based on one pdf file")

st.sidebar.header("Document")

file = st.sidebar.file_uploader("Input a PDF file", type='pdf')

# Initialise a RecursiveCharacterTextSplitter to split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    separators = "\n",            # Use newline characters as the separators for splitting the text
    chunk_size = 1000,            # Set the maximum size of each chunk to 1000 characters
    chunk_overlap = 150,          # Ensure that 150 characters overlap between consecutive chunks
    length_function = len         # Use the len function to calculate the length of the text
)

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    chunks = text_splitter.split_text(text)
    st.write(chunks)
else:
    st.write("Input a file...")


