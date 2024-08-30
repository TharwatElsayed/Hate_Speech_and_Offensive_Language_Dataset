import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('labeled_data.csv')

# Set Streamlit page title
st.title('Hate Speech and Offensive Language Analysis')

# Horizontal line separator
st.markdown("---")

# Create tabs
tab1, tab2 = st.tabs(["Dataset Overview", "Dataset Description", "Dataset Information"])

# Tab 1: Dataset Overview
with tab1:
    st.subheader('Dataset Overview (Before Preprocessing)')
    st.write(df.head(10))

# Tab 2: Dataset Columns Description
with tab2:
    st.subheader('Dataset Columns Description')
    st.write(df.describe(include='all'))

# Tab 3: Dataset Brief Information
with tab2:
    st.subheader('Dataset Brief Information')
    st.write(df.info())

# Horizontal line separator
st.markdown("---")

# Create a radio button for chart selection
chart_type = st.radio("Choose Chart Type", ('Bar Chart', 'Pie Chart'))

# Display the selected chart
if chart_type == 'Bar Chart':
    st.subheader('Distribution of Classes (Bar Chart)')
    plt.figure(figsize=(8, 6))
    plt.hist(df['class'], bins=3, edgecolor='black')
    plt.xlabel('Class')
    plt.ylabel('Frequency')
    plt.title('Distribution of Classes')
    plt.xticks([0, 1, 2], ['Hate Speech', 'Offensive Language', 'Neither'])
    st.pyplot(plt)

elif chart_type == 'Pie Chart':
    st.subheader('Proportion of Classes (Pie Chart)')
    labels = 'Hate Speech', 'Offensive Language', 'Neither'
    sizes = df['class'].value_counts()
    explode = (0, 0.1, 0)  # only "explode" the 2nd slice
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Distribution of Classes')
    st.pyplot(plt)

# Horizontal line separator
st.markdown("---")
