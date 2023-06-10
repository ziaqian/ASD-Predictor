import streamlit as st
import pandas as pd


st.set_page_config(page_title="Liver Predictor",page_icon="🧑‍⚕️")
#Function to display the content in the Home Page
st.title("LIVER DISEASE INFO")
st.sidebar.success("Select a page above")

st.subheader("ABOUT LIVER DISEASE")

st.text("")
st.write(
    """

    Below is  a picture of the various condition of a liver 

    """
    )  
st.image("Liver.png")
st.text("")
st.write(
    """ 
        Your liver is your body’s second-largest organ. It sits just under your ribcage on the right side and is about the size of a football. The liver separates nutrients and waste as they move through your digestive system. It also produces bile, a substance that carries toxins out of your body and aids in digestion.

        The term “liver disease” refers to any of several conditions that can affect and damage your liver. Over time, liver disease can cause cirrhosis (scarring). As more scar tissue replaces healthy liver tissue, the liver can no longer function properly. Left untreated, liver disease can lead to liver failure and liver cancer.

    """
    )    
st.text("")


st.write("---")
st.text("")
st.subheader("RISK FACTORS OF CAUSING LIVER DISEASE")
st.text("")
st.write(
    """
    * Heavy alcohol use

    * Obesity

    * Type 2 diabetes

    * Tattos or body piercing

    * Injecting drugs using shared needles

    * Exposure to other people's blood and body fluids

    * Unprotected sex

    * Exposure to certain chemicals or toxins

    * Family history
    """
    )
st.text("")


st.subheader("CAUSES OF DIFFERENT TYPES OF LIVER DISEASE")
st.text("")
d = {"Cause": ["Infection", "Immune system abnormality", "Genetics", "Cancer and other growth", "Conduming too many toxins"],
         'Type': ["Hepatitis A, Hepatitis B, Hepatitis C", "Autoimmune hepatitis, Primary biliary cholangitis, Primary sclerosing", "Hemochromatosis, Wilson's disease, Alpha-1 antitypsin deficiency", "Liver cancer, Bile duct cancer, Liver adenoma", "Alcohol-related fatty liver disease, Non-alcohol related fatty liver"]}
df = pd.DataFrame(data=d, index=[1, 2, 3, 4, 5])
st.table(df)
st.text("")
st.text("")


st.subheader("SYMPTOMS")
st.text("")
st.write(
    """
    * Abdominal pain (especially on the right side)

    * Bruising easily

    * Changes in the colour of urine

    * Fatigue

    * Nause/ vomitting

    * Swelling in arms and legs

    * Skin and eye appear yellow

    * Itchy skin

    * Loss of apetite
     """
     )
st.text("")


st.subheader("DIAGNOSIS AND TEST")
st.text("")
d = {"Test": ["Blood Test", "Imaging test", "Liver biopsy"],
         'Type': ["Liver enzyme meansure, international normalized ration (INR)", "ultrasound, MRI, CT scan","-"]}
df = pd.DataFrame(data=d, index=[1, 2, 3])
st.table(df)
st.text("")


st.subheader("TREATMENT")
st.text("")
st.write(
    """
    * Medication         : viral infection, inherited conditions

    * Lifestyle changes  : Alcohol-related liver disease

    * Liver transplant   : liver failure
    """
    )
st.text("")


st.subheader("PREVENTION")
st.text("")
st.write(
    """
    * Avoid alcohol

    * Avoid food and drinks with trans fats or high-fructose corn syrup

    * Manage medicationintake

    * regular exercise

    * Limit consumption of red meaat
    """
    )
st.text("")

# Display the questionnaires and predict result based on user's input
def predictionResult():
    st.subheader("Predictor")
    st.write("Please fill all the questions below ")
    st.text("")
