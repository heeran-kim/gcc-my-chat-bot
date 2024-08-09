"""
This simple chatbot application allows users to upload a PDF file and extracts the text content from it.
The extracted text is then displayed on the web page.

Libraries used:
- Streamlit: For creating the web interface.
- PyPDF2: For reading and extracting text from PDF files.

Features:
- PDF File Upload: Users can upload a PDF file via the sidebar.
- Text Extraction: The app extracts text from each page of the PDF and displays it.
- User Prompt: If no file is uploaded, the app prompts the user to upload a file.
"""
import streamlit as st
from PyPDF2 import PdfReader

st.header("A simple chat bot based on one pdf file")

st.sidebar.header("Document")

file = st.sidebar.file_uploader("Input a PDF file", type='pdf')

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    st.write(text)
else:
    st.write("Input a file...")
