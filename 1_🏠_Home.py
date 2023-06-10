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
st.header("Limitation of the Model")
st.write(
 """
  * The prediction model provides a binary result indicating whether or not a patient is likely to have liver disease based on the available data and variables. However, it is important to note that it does not provide a probability of getting liver disease. For further confirmation, extra tests need to be conducted if needed. 
  
  * The prediction model is based on the available data and variables used in the analysis. There may be other important factors that were not included in the analysis, which could affect the accuracy of the prediction.
  
  * The website does not provide a diagnosis or treatment plan. The treatment plan should be executed based on patients' bodies' condition in real life and their medical history. Professional advice from medical professional is needed to treat the disease. 
  
  * It is important to note that this website is used as a tool to supplement and not replace medical advice from medical professional. It should not be considered as a substitute for medical advice or consultation with a health care provider for proper evaluation and diagnosis.
  
  * This website does not provided a comprehensive assessment of a person's overall health as overall health does not solely based on the condition of liver.

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
