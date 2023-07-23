import streamlit as st

def render_english():
    # Set dark theme
    st.markdown("""
        <style>
        body {
            color: white;
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
    st.markdown("[Visualization 1](/page1)")
    st.markdown("[Visualization 2](/page2)")
    st.markdown("[Visualization 3](/page3)")

def render_french():
    # Set dark theme
    st.markdown("""
        <style>
        body {
            color: white;
            background-color: #1F2937;
        }
        </style>
        """, unsafe_allow_html=True)

    # Background image (you can remove this line if you don't have a background image)
    # st.image("background.jpg", use_column_width=True)

    # Profile photo and description
    st.title("Votre Nom")
    st.subheader("Ingénieur en Télécommunications, Data Science")
    st.markdown("[GitHub](https://github.com/votre-github) [LinkedIn](https://linkedin.com/in/votre-linkedin)")

    # Links to other pages
    st.subheader("Visualisations")
    st.markdown("[Visualisation 1](/page1)")
    st.markdown("[Visualisation 2](/page2)")
    st.markdown("[Visualisation 3](/page3)")

def render_spanish():
    # Set dark theme
    st.markdown("""
        <style>
        body {
            color: white;
            background-color: #1F2937;
        }
        </style>
        """, unsafe_allow_html=True)

    # Background image (you can remove this line if you don't have a background image)
    # st.image("background.jpg", use_column_width=True)

    # Profile photo and description
    st.title("Tu Nombre")
    st.subheader("Ingeniero de Telecomunicaciones, Data Science")
    st.markdown("[GitHub](https://github.com/tu-github) [LinkedIn](https://linkedin.com/in/tu-linkedin)")

    # Links to other pages
    st.subheader("Visualizaciones")
    st.markdown("[Visualización 1](/page1)")
    st.markdown("[Visualización 2](/page2)")
    st.markdown("[Visualización 3](/page3)")

# Language selection
language = st.sidebar.selectbox("Language", ["English", "Français", "Español"])

# Render page based on selected language
if language == "English":
    render_english()
elif language == "Français":
    render_french()
elif language == "Español":
    render_spanish()
