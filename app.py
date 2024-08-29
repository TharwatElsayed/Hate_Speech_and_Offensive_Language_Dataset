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

# Assuming 'class' is the name of the column you want to create a histogram for
# Create the plot
plt.figure(figsize=(8, 6))
plt.hist(df['class'], bins=3, edgecolor='black')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.title('Distribution of Classes')
plt.xticks([0, 1, 2], ['Hate Speech', 'Offensive Language', 'Neither'])

# Display the plot in Streamlit
st.pyplot(plt)
