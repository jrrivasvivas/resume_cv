import streamlit as st
from PIL import Image

def render_english():
    # Set dark theme
    st.markdown(
        """
        <style>
        body {
            color: white;
            background-color: #1F2937;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Background image
    background_image = Image.open("background.jpg")
    st.image(background_image, use_column_width=True)

    # Profile photo and description
    col1, col2 = st.beta_columns([1, 4])
    with col1:
        profile_image = Image.open("profile.jpg")
        st.image(profile_image, width=150)
    with col2:
        st.title("Your Name")
        st.subheader("Telecommunications Engineer, Data Science")
        st.markdown("[GitHub](https://github.com/your-github) [LinkedIn](https://linkedin.com/in/your-linkedin)")

    # Links to other pages
    st.subheader("Visualizations")
    col3, col4, col5 = st.beta_columns(3)
    with col3:
        image1 = Image.open("image1.jpg")
        st.image(image1, use_column_width=True)
        st.markdown("[Visualization 1](/page1)")
    with col4:
        image2 = Image.open("image2.jpg")
        st.image(image2, use_column_width=True)
        st.markdown("[Visualization 2](/page2)")
    with col5:
        image3 = Image.open("image3.jpg")
        st.image(image3, use_column_width=True)
        st.markdown("[Visualization 3](/page3)")

# Resto del código para renderizar en otros idiomas

# Language selection
language = st.sidebar.selectbox("Language", ["English", "Français", "Español"])

# Render page based on selected language
if language == "English":
    render_english()
# Resto del código para renderizar en otros idiomas
