import streamlit as st

# Set dark theme
st.markdown("""
    <style>
    body {
        color: black;
        background-color: #1F2937;
    }
    </style>
    """, unsafe_allow_html=True)

# Background image (you can remove this line if you don't have a background image)
# st.image("background.jpg", use_column_width=True)

# Profile photo and description
st.title("Your Name")
st.subheader("Telecommunications Engineer, Data Science")
st.markdown("[GitHub](https://github.com/your-github) [LinkedIn](https://linkedin.com/in/your-linkedin)")

# Links to other pages
st.subheader("Visualizations")
st.markdown("[Visualization 1](/page1) - A scatter plot with random data using scikit-learn and Plotly.")
st.markdown("[Visualization 2](/page2) - Placeholder for Visualization 2.")
st.markdown("[Visualization 3](/page3) - Placeholder for Visualization 3.")

# Page 1 - Visualization with scatter plot
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

if st.session_state.page == 'page1':
    # Import and run the code for Page 1
    from pages import page1
elif st.session_state.page == 'page2':
    # Import and run the code for Page 2
    from pages import page2
elif st.session_state.page == 'page3':
    # Import and run the code for Page 3
    from pages import page3
