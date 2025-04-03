import streamlit as st
import sklearn
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Student Performance")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)
Previous_Scores = st.slider('How many marks scored in previous exams', 0,100, 50)
num_input_previous = st.number_input("Insert the Previous Score", min_value=0, max_value=100, value=Previous_Scores)
user_input = [[Previous_Scores]]

if st.button('Predict?'):
    st.write("The model predicts the student performance:", model.predict(user_input).round(2))
