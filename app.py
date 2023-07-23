# Importación de bibliotecas
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Definición de una función para generar datos aleatorios
def generate_random_data(size=100, columns=['X', 'Y']):
    data = np.random.rand(size, len(columns))
    return pd.DataFrame(data, columns=columns)

# Configuración del tema
st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="📊",
    theme={"primaryColor":"#F63366","backgroundColor":"#0E1117","secondaryBackgroundColor":"#31333F","textColor":"#FFFFFF","font":"sans serif"}
)

# Creación de la página de inicio
st.title("Tu Nombre")
st.subheader("Tu Profesión")
st.markdown("GitHub: [Enlace](https://github.com/username)")
st.markdown("LinkedIn: [Enlace](https://www.linkedin.com/in/username)")

# Creación de enlaces a las visualizaciones
st.subheader("Visualizaciones")
st.markdown("[Visualización 1](/page1)")
st.markdown("[Visualización 2](/page2)")
st.markdown("[Visualización 3](/page3)")

# Creación de las visualizaciones
page = st.experimental_get_query_params().get("page", None)
if page:
    if page[0] == 'page1':
        st.title("Visualización 1")
        st.text("Este es un scatter plot con datos aleatorios utilizando Plotly")
        df = generate_random_data()
        fig = px.scatter(df, x='X', y='Y')
        st.plotly_chart(fig)
    elif page[0] == 'page2':
        st.title("Placeholder para Visualización 2")
    elif page[0] == 'page3':
        st.title("Placeholder para Visualización 3")