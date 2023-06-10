import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Load your analysis data
df = pd.read_csv(r"C:\Users\60111\Documents\WIE 2003- IDS\IDS GROUP PROJECT\ASD_data.csv")

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
