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

    # Background image
    st.image("background.jpg", use_column_width=True)

    # Profile photo and description
    col1, col2 = st.beta_columns([1, 4])
    with col1:
        st.image("profile.jpg", width=150)
    with col2:
        st.title("Your Name")
        st.subheader("Telecommunications Engineer, Data Science")
        st.markdown("[GitHub](https://github.com/your-github) [LinkedIn](https://linkedin.com/in/your-linkedin)")

    # Links to other pages
    st.subheader("Visualizations")
    col3, col4, col5 = st.beta_columns(3)
    with col3:
        st.image("image1.jpg", use_column_width=True)
        st.markdown("[Visualization 1](/page1)")
    with col4:
        st.image("image2.jpg", use_column_width=True)
        st.markdown("[Visualization 2](/page2)")
    with col5:
        st.image("image3.jpg", use_column_width=True)
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

    # Background image
    st.image("background.jpg", use_column_width=True)

    # Profile photo and description
    col1, col2 = st.beta_columns([1, 4])
    with col1:
        st.image("profile.jpg", width=150)
    with col2:
        st.title("Votre Nom")
        st.subheader("Ingénieur en Télécommunications, Data Science")
        st.markdown("[GitHub](https://github.com/votre-github) [LinkedIn](https://linkedin.com/in/votre-linkedin)")

    # Links to other pages
    st.subheader("Visualisations")
    col3, col4, col5 = st.beta_columns(3)
    with col3:
        st.image("image1.jpg", use_column_width=True)
        st.markdown("[Visualisation 1](/page1)")
    with col4:
        st.image("image2.jpg", use_column_width=True)
        st.markdown("[Visualisation 2](/page2)")
    with col5:
        st.image("image3.jpg", use_column_width=True)
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

    # Background image
    st.image("background.jpg", use_column_width=True)

    # Profile photo and description
    col1, col2 = st.beta_columns([1, 4])
    with col1:
        st.image("profile.jpg", width=150)
    with col2:
        st.title("Tu Nombre")
        st.subheader("Ingeniero de Telecomunicaciones, Data Science")
        st.markdown("[GitHub](https://github.com/tu-github) [LinkedIn](https://linkedin.com/in/tu-linkedin)")

    # Links to other pages
    st.subheader("Visualizaciones")
    col3, col4, col5 = st.beta_columns(3)
    with col3:
        st.image("image1.jpg", use_column_width=True)
        st.markdown("[Visualización 1](/page1)")
    with col4:
        st.image("image2.jpg", use_column_width=True)
        st.markdown("[Visualización 2](/page2)")
    with col5:
        st.image("image3.jpg", use_column_width=True)
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
