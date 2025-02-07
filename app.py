import streamlit as st
import datetime

#name
title = st.text_input("Name: ", "Su Shar Lae")
st.write("My name is", title)

#DoB
d = st.date_input("Birthday", datetime.date(2019, 7, 6))
st.write("My birthday is on", d)

#height
number = st.number_input('Height (approximate in ft): ')
st.write('I am' ,number, 'feet tall')

#address
option = st.selectbox(
    "City: ",
    ("Yangon", "Mandalay", "Moggok"),
)
st.write("I live in", option)

#color
color = st.color_picker("Favorite Color", "#00f900")
st.write("My favorite color is", color)

#rating
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
else: 
    ("Please select one to continue")

