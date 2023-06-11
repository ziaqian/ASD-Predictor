import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px


st.set_page_config(page_title="ASD Predictor",page_icon="🧑‍⚕️")
#Function to display the content in the Home Page
st.title("Analysis")
st.sidebar.success("Select a page above")

# Load your analysis data
df = pd.read_csv("ASD_data.csv")

# Define custom colors for the graphs
custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3']


def display_analysis():
    st.subheader("ANALYSIS OF ASD DATASETS")
    plot_ethnicity()
    plot_gender()
    plot_age()
    plot_country_of_residence()
    plot_jaundice()
    plot_age1()

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
    
def plot_age1():
    # Filter data for people diagnosed with ASD
    asd_1_data = df[df['Class/ASD'] == 1]

    fig = px.histogram(asd_1_data, x='Age', histnorm='density', nbins=10, title='ASD by Age',
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
    
def plot_jaundice():
    jaundice_counts = df.groupby(['Jaundice', 'Class/ASD']).size().reset_index(name='Count')
    fig = px.bar(jaundice_counts, x='Jaundice', y='Count', color='Class/ASD', barmode='group',
                 color_discrete_sequence=custom_colors,
                 labels={'Jaundice': 'Jaundice', 'Count': 'Count', 'Class/ASD': 'ASD Diagnosis'})
    fig.update_layout(title='ASD by Jaundice', xaxis_title='Jaundice', yaxis_title='Count')
    st.plotly_chart(fig)

display_analysis()
