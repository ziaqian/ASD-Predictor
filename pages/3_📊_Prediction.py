import streamlit as st
import pickle
import numpy as np
import sklearn

st.set_page_config(page_title="ASD Predictor",page_icon="🧑‍⚕️")
st.title("ASD PREDICTION")
st.sidebar.success("Select a page above")
st.write("---")
st.text("")

st.subheader('ASD Prediction Test')
st.markdown('Answer the following 10 questions to predict the likelihood of having ASD. Select 1 for agree; 0 for disagree. ')
    
# Input scores
a1 = st.selectbox("1) I often notice small sounds when others do not.", [0, 1])
a2 = st.selectbox("2) I usually concentrate more on the whole picture, rather than the small details.", [0, 1])
a3 = st.selectbox("3) I find it easy to do more than one thing at once.", [0, 1])
a4 = st.selectbox("4) If there is an interruption, I can switch back to what I was doing very quickly.", [0, 1])
a5 = st.selectbox("5) I find it easy to 'read between the lines' when someone is talking to me.", [0, 1])
a6 = st.selectbox("6) I know how to tell if someone listening to me is getting bored.", [0, 1])
a7 = st.selectbox("7) When I'm reading a story, I find it difficult to work out the character's intention.", [0, 1])
a8 = st.selectbox("8) I like to collect information about categories of things (e.g. types of car, types of bird, types of train, types of plant, etc.)", [0, 1])
a9 = st.selectbox("9) I find it easy to work out what someone is thinking or feeling just by looking at their face.", [0, 1])
a10 = st.selectbox("10) I find it difficult to work out people’s intentions.", [0, 1])
    
# Add a button to predict
if st.button("Predict"):
  # Calculate total score
  total_score = a1 + (1 - a2) + (1 - a3) + (1 - a4) + (1 - a5) + (1 - a6) + a7 + a8 + (1 - a9) + a10
  result=""
  # Determine prediction result
  if total_score >= 6:
    result="The patient has higher possibility to have autism."
  else:
    result="The patient has lower possibility to have autism."
    
  st.code(result)
  st.text("")
