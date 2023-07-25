import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def generate_random_data():
    np.random.seed(0)
    data = np.random.randn(100, 2)
    df = pd.DataFrame(data, columns=['X', 'Y'])
    return df

st.subheader("Visualization 1")
st.write("A scatter plot with random data using scikit-learn and Plotly.")

# Generate random data
df = generate_random_data()

# Scatter plot using Plotly
fig = px.scatter(df, x='X', y='Y', title='Scatter Plot with Random Data')
st.plotly_chart(fig)
