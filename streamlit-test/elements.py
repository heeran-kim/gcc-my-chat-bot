# Run: streamlit run elements.py

import streamlit as st

# selectbox
st.header("Selectbox")

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Breen')
)

st.write('Your favorite color is ', option)

# multiselects
st.header("Multiselects")

options = st.multiselect(
    'What are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue']
)

st.write('Your favorite colors are ', options)

# checkbox
st.header("Checkbox")

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
ice = st.checkbox('ice')

if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Great! Here's some more ☕")

if ice:
    st.write("Great! Here's some more 🧊")