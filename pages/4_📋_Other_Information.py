import streamlit as st
import pandas as pd

st.set_page_config(page_title="ASD Predictor",page_icon="🧑‍⚕️")
#Function to display the content in the Home Page
st.title("OTHER INFORMATION")
st.sidebar.success("Select a page above")

st.subheader("What is Autism?")
st.image("what-is-autism-spectrum-disorder.jpg")
st.write("Autism, or Autism Spectrum Disorder (ASD), is a neurodevelopmental disorder that typically appears in early childhood and lasts throughout a person's lifetime. It affects how individuals perceive the world, interact with others, and communicate.")

st.subheader('Signs and Symptoms of Autism')
st.markdown("- Difficulties in social interaction")
st.markdown("- Communication challenges")
st.markdown("- Repetitive behaviors")
st.markdown("- Sensory sensitivities")
st.markdown("- Specific interests or fixations")
st.write("It's important to remember that autism is a spectrum disorder, and each individual may exhibit a unique combination of strengths and difficulties.")
st.write("")

st.subheader('Early Detection and Diagnosis')
st.write("Early detection and diagnosis of autism can be crucial for accessing appropriate interventions and support. If you suspect that your child or someone you know may have autism, it's recommended to consult with a healthcare professional, such as a pediatrician or a developmental specialist, who can conduct a comprehensive evaluation.")
st.write("")    

st.subheader('Treatment and Support')
st.write("Early intervention and appropriate support for individuals with autism can make a significant difference in their quality of life. Treatment approaches may include behavioral therapies, speech therapy, occupational therapy, and educational interventions tailored to the individual's specific needs.")
st.write("")
st.write("Creating a supportive environment for individuals with autism is essential. This can include fostering understanding and acceptance, promoting inclusive education and employment opportunities, and providing access to community resources and support groups. It is important to recognize and respect the unique strengths and challenges of each individual with autism.")
st.write("")    

st.subheader('Additional Resources')
st.write("If you would like to learn more about autism or seek support, here are some reputable organizations and resources:")
st.write("- Autism Speaks (https://www.autismspeaks.org/)")
st.write("- Autism Society (https://www.autism-society.org/)")
st.write("- National Autistic Society (https://www.autism.org.uk/)")
st.write("- Centers for Disease Control and Prevention - Autism Information (https://www.cdc.gov/ncbddd/autism/index.html)")
st.write("")    
