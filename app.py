import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('labeled_data.csv')

# Set Streamlit page title
st.title('Hate Speech and Offensive Language Analysis')

# Horizontal line separator
st.markdown("---")

# Display basic dataset information
st.subheader('Dataset Overview (Before Preprocessing)')
st.write(df.describe(include='all'))

# Horizontal line separator
st.markdown("---")

# Count the occurrences of each class
class_counts = df['class'].value_counts()
# Create a bar chart
fig_bar = px.bar(x=class_counts.index, y=class_counts.values, 
                 labels={'x': 'Class', 'y': 'Count'},
                 title='Distribution of Classes')

# Create a pie chart
fig_pie = px.pie(names=class_counts.index, values=class_counts.values,
                 title='Proportion of Classes')

# Bar chart
st.subheader('Distribution of Classes (Bar Chart)')
st.plotly_chart(fig_bar)

# Pie chart
st.subheader('Proportion of Classes (Pie Chart)')
st.plotly_chart(fig_pie)

# Horizontal line separator
st.markdown("---")

