import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('labeled_data.csv')

# Set Streamlit page title
st.title('Hate Speech and Offensive Language Analysis')

# Display basic dataset information
st.subheader('Dataset Overview')
st.write(df.describe())
