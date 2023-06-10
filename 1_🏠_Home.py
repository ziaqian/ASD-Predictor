import streamlit as st
import pandas as pd

st.set_page_config(page_title="ASD Predictor",page_icon="🧑‍⚕️")
#Function to display the content in the Home Page
st.title("HOME")
st.sidebar.success("Select a page above")

st.text("")
st.subheader("Introduction")
st.write(
 """
Welcome to the Autism Spectrum Disorder(ASD) Predictor Project homepage! 
 
Our ASD Predictor application is an innovative tool designed to assist in the prediction of Autism Spectrum Disorder (ASD) in adults. We understand the importance of early detection and intervention to improve the well-being and quality of life for individuals with ASD.
 
We have conducted extensive research and analysis to develop a robust prediction model for the public. Our findings are based on comprehensive data analysis, including behavioral characteristics, communication patterns, social interactions, and other relevant factors associated with ASD.
 """
)

st.text("")
st.write("---")
st.text("")
st.subheader("Problem Statement")
st.write(
 """
Autism Spectrum Disorder (ASD) affects a significant number of individuals, with an estimated prevalence of 1 in 54 children in the United States. However, many cases of ASD go undiagnosed until later in life, leading to delayed intervention and support.

Early detection and diagnosis of ASD in adulthood are crucial for individuals to receive appropriate interventions, therapies, and support services. However, there is a need to improve the identification and prediction of ASD, as it can be challenging to recognize the symptoms and distinguish them from other conditions.
 
Therefore, our problem statement is how can we use machine learning to help in predicting ASD for early detection.
 """   
)
st.text("")
st.write("---")
st.text("")
st.subheader("Goal")
st.write(
 """
 * Diagnosis support: Provide individuals and healthcare professionals with a reliable tool to aid in the identification and referral process.

 * Early detection: Early detection can help in improving the quality of life of individuals with ASD. 
 
 * Data analysis: Presents data on the realationship between different variables, provide a glimpse into the patterns and trends of ASD.
 
 * Improve Access to Services: To connect individuals with ASD to specialized services and support networks.
 """   
)
st.text("")
st.write("---")
st.text("")
st.header("Limitations")
st.write(
 """
  * Our prediction model relies on the available data and variables utilized in the analysis. However, it is important to note that there may be additional significant factors not accounted for in the analysis, potentially impacting the accuracy of the predictions.
  
  * The apllication should be viewed as a screening tool and not a diagnostic tool. It can provide insights and indications regarding the likelihood of ASD, but it cannot replace a comprehensive evaluation conducted by qualified healthcare professionals for a definitive diagnosis.
 
 """
)
st.text("")
st.write("---")
st.text("")
st.subheader("Our Team")
st.write(
 """
 * AKMAL HAZIQ BIN SHARIP

 * CARMEN LAM KAH MAN

 * DERNICE LEE TIAN YI

 * ESTHER LOH YUN HAN

 * LEE ZIA QIAN
 """   
)
st.text("")
st.write("---")
st.text("")
st.markdown("<h2 style='text-align: center; color: grey;'>\"ASD Predictor: Empowering Early Intervention, Unleashing Potential", unsafe_allow_html=True)
