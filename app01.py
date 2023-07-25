# 1. Library Imports
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# 2. Definition of a Function to Generate Random Data
def generate_random_data():
    data = np.random.rand(100,2)
    df = pd.DataFrame(data, columns=['X', 'Y'])
    return df

# 3. Theme Configuration
# As of my knowledge cutoff in September 2021, Streamlit does not support theme customization via CSS. 
# You would have to use Streamlit's built-in theme options or customize the UI with the help of markdown and HTML in python.

# 4. Definition of Functions for Each Page
def render_landing_page():
    st.title("Your Name")
    st.subheader("Your Profession")
    st.markdown("GitHub: [Your GitHub Link]")
    st.markdown("LinkedIn: [Your LinkedIn Link]")

def render_visualization1():
    st.title("Visualization 1")
    df = generate_random_data()
    fig = px.scatter(df, x='X', y='Y')
    st.plotly_chart(fig)

def render_visualization2():
    st.title("Visualization 2")
    st.text("Placeholder")

# 5. Sidebar for Navigation
st.sidebar.title('Navigation')
options = ["Landing Page", "Visualization 1", "Visualization 2"]
choice = st.sidebar.radio("Go to", options)

# Dictionary of Pages 
pages = {
    "Landing Page": render_landing_page,
    "Visualization 1": render_visualization1,
    "Visualization 2": render_visualization2,
}

# Rendering the Selected Page
pages[choice]()