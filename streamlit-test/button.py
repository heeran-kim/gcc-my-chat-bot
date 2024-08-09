# Run: streamlit run button.py

import streamlit as st

st.header('Button Test Page: st.button')

if st.button("Say Hello"):
    st.write("See hello here..")
else:
    st.write("Good bye.")
