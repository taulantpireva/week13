import streamlit as st
import pandas as pd
import seaborn as sns

# Set the page configuration
st.set_page_config(page_title="Iris Dataset Streamlit App")

# Load data
@st.cache_data
def load_data():
    return sns.load_dataset("iris")

data = load_data()

# Title and description
st.title("Iris Dataset Streamlit App")
st.write("This app demonstrates a simple Streamlit application with data visualization and interactivity using the Iris dataset.")

# Radio buttons to select X and Y axes for the scatter plot
col1, col2 = st.columns(2)

with col1:
    x_axis = st.radio("Choose X-axis", options=data.columns, index=0)

with col2:
    y_axis = st.radio("Choose Y-axis", options=data.columns, index=1)

# Create a scatter plot
st.subheader("Scatter Plot")
st.write(f"Scatter plot of {x_axis} vs {y_axis}")
scatter_plot = sns.scatterplot(x=x_axis, y=y_axis, data=data)
st.pyplot(scatter_plot.figure)

# Interactive widgets
st.subheader("Display Data")

# Slider to select the number of rows to display
num_rows = st.slider("Select number of rows to display", 1, len(data), 10)
st.write(f"Displaying the first {num_rows} rows of the dataset")
st.write(data.head(num_rows))

# Checkbox to show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)
