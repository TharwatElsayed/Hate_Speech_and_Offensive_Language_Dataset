import streamlit as st
import pandas as pd
import plotly.express as px
from google.colab import drive

# Load the dataset
df = pd.read_csv('labeled_data.csv')

# Set Streamlit page title
st.title('Hate Speech and Offensive Language Analysis')

# Display basic dataset information
st.subheader('Dataset Overview')
st.write(df.describe())

# Visualizations
st.subheader('Visualizations')

# Class Distribution
class_counts = df['class'].value_counts()
fig_class_dist = px.bar(class_counts, x=class_counts.index, y=class_counts.values,
                         labels={'x': 'Class', 'y': 'Count'},
                         title='Distribution of Classes')
st.plotly_chart(fig_class_dist)

# Word Count Distribution
df['word_count'] = df['tweet'].apply(lambda x: len(x.split()))
fig_word_count = px.histogram(df, x='word_count', title='Distribution of Word Counts')
st.plotly_chart(fig_word_count)
