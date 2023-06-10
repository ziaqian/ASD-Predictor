import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Load your analysis data
df = pd.read_csv("ASD_data.csv")

# Define custom colors for the graphs
custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3']

def run_website():
    st.sidebar.title('ASD Analysis')
    selected = st.sidebar.button('Homepage')
    if selected:
        display_homepage()

    selected = st.sidebar.button('Analysis')
    if selected:
        display_analysis()

    selected = st.sidebar.button('Prediction')
    if selected:
        display_prediction()

    selected = st.sidebar.button('Other Information')
    if selected:
        display_other_information()

def display_homepage():
    st.title('Homepage')
    # Add content for the homepage
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
    st.markdown("<h2 style='text-align: center; color: grey;'>\"Empowering Early Intervention, Unleashing Potential\"</h2>", unsafe_allow_html=True)

def display_analysis():
    st.title('Analysis of data sets')
    plot_ethnicity()
    plot_gender()
    plot_age()
    plot_country_of_residence()

def display_prediction():
    st.title('ASD Prediction Test')
    st.markdown('Answer the following 10 questions to know the scores and predict the likelihood of having ASD.')
    # Add content for the prediction page

def display_other_information():
    st.title('Other Information')
    # Add content for the other information page

def plot_ethnicity():
    ethnicity_counts = df['Ethnicity'].value_counts()
    fig = px.bar(x=ethnicity_counts.index, y=ethnicity_counts.values, color=ethnicity_counts.index,
                 color_discrete_sequence=custom_colors)
    fig.update_layout(title='ASD by Ethnicity', xaxis_title='Ethnicity', yaxis_title='Count')
    fig.update_xaxes(type='category')  # Set x-axis type to 'category'
    st.plotly_chart(fig)

def plot_gender():
    gender_mapping = {'f': 'Female', 'm': 'Male'}  # Update the gender mapping
    df['Gender'] = df['Gender'].map(gender_mapping)
    gender_counts = df['Gender'].value_counts()
    fig = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index,
                 title='ASD by Gender', color=gender_counts.index, color_discrete_sequence=custom_colors)
    st.plotly_chart(fig)

st.set_option('deprecation.showPyplotGlobalUse', False)

def plot_age():
    fig = px.histogram(df, x='Age', histnorm='density', nbins=10, title='ASD by Age',
                       color_discrete_sequence=[custom_colors[0]])
    fig.update_traces(opacity=0.7)  # Adjust the opacity of the bars
    fig.update_layout(title='ASD by Age', xaxis_title='Age', yaxis_title='Density')
    st.plotly_chart(fig)

def plot_country_of_residence():
    country_counts = df['Country_Of_Residence'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    fig = px.sunburst(country_counts, path=['Country'], values='Count', title='ASD by Country of Residence')
    fig.update_traces(textinfo='label+percent entry')
    fig.update_layout(width=800, height=600, margin=dict(t=30, l=0, r=0, b=0))
    fig.update_layout(clickmode='event+select')  # Enable click events on the chart
    st.plotly_chart(fig)

# Streamlit app
st.title('ASD Analysis')
run_website()
