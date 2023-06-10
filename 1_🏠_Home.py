import streamlit as st
import pandas as pd

st.set_page_config(page_title="Liver Predictor",page_icon="🧑‍⚕️")
#Function to display the content in the Home Page
st.title("ABOUT US")
st.sidebar.success("Select a page above")

st.text("")
st.subheader("BLues CLues")
st.write(
 """
 BLues CLues is a group of 5 students who are taking the subject of Machine Learning in University of Malaya.
 
The name BLues CLues is inspired by the TV show Blue's Clues.The show follows an animated blue-spotted dog named Blue as she leaves a trail of clues/paw prints for the host and the viewers to figure out her plans for the day.

 """
)


st.write(
 """
 Therefore, our aim is to solve puzzles based on the clues there are.
 
 In this project, BLues CLues has created a Liver Disease Predictor. Below are the problem statement, objectives, limitations and group members of the project:
 """
)
st.text("")
st.write("---")
st.text("")
st.subheader("Problem Statement")
st.write(
 """
Overall, about 1 in 10 Americans (30 million in total) have some type of liver disease. About 5.5 million people in the U.S. have chronic liver disease or cirrhosis.

Some types of liver disease are becoming more common in the U.S. because they are related to rising rates of obesity. An estimated 20% to 30% of adults have excess fat in their liver, a condition called non-alcohol rekated fatty liver disease (NAFD). This may be renamed metabolic-associated fatty liver disease (MAFLD) to reflect its relationship to metabolic syndrome and conditions like diabetes, high blood pressure, high cholesterol and obesity.
 
Therefore, our problem statement is how can we use machine learning to help in predicting liver disease for early detection.
 """   
)
st.text("")
st.write("---")
st.text("")
st.subheader("Objective")
st.write(
 """
 * Diagnosis support: To provide a tool for professionals to verify their diagnoses and reduce errors in diagnosis.

 * Early detection: Early detection can help in preventing the progression of the disease and increase recovery chance. 
 
 * To assist in the diagnosis of complex and confusing medical data by providing an easy-to-use and accurate tool.
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
 * Adeline Kong Earn Ning

 * Lee Zia Qian

 * Low Hui Yi

 * Tang Yuen Yin

 * Yoong Jing Yi 
 """   
)
st.text("")
st.write("---")
st.text("")
st.markdown("<h2 style='text-align: center; color: grey;'>\"Clues bring us one step closer to the Truth\"</h2>", unsafe_allow_html=True)
