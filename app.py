import streamlit as st
from PIL import Image

# Cargar imágenes
background_image = Image.open('background_image.jpg')
profile_image = Image.open('profile_image.jpg')

# Definir diccionarios para la traducción
english_dict = {
    'title': 'Telecommunications Engineer',
    'desc': 'Data Science, driven by curiosity',
    'github': 'https://www.github.com/your_username',
    'linkedin': 'https://www.linkedin.com/in/your_username',
    'projects': 'Projects'
}

french_dict = {
    'title': 'Ingénieur en télécommunications',
    'desc': 'Science des données, animé par la curiosité',
    'github': 'https://www.github.com/your_username',
    'linkedin': 'https://www.linkedin.com/in/your_username',
    'projects': 'Projets'
}

spanish_dict = {
    'title': 'Ingeniero de Telecomunicaciones',
    'desc': 'Ciencia de Datos, movido por la curiosidad',
    'github': 'https://www.github.com/your_username',
    'linkedin': 'https://www.linkedin.com/in/your_username',
    'projects': 'Proyectos'
}

# Opción de idioma
language_option = st.sidebar.selectbox('Language', options=['English', 'Français', 'Español'])

if language_option == 'English':
    lang_dict = english_dict
elif language_option == 'Français':
    lang_dict = french_dict
else:
    lang_dict = spanish_dict

# Página de inicio
st.title(lang_dict['title'])
st.image(profile_image, use_column_width=True)
st.write(lang_dict['desc'])
st.markdown(f"[Github]({lang_dict['github']})")
st.markdown(f"[LinkedIn]({lang_dict['linkedin']})")

# Proyectos
st.header(lang_dict['projects'])
project_images = ['project1.jpg', 'project2.jpg', 'project3.jpg', 'project4.jpg', 'project5.jpg', 'project6.jpg']
project_links = ['project1_link', 'project2_link', 'project3_link', 'project4_link', 'project5_link', 'project6_link']

for i in range(len(project_images)):
    if st.button(lang_dict['projects'] + str(i+1)):
        st.image(project_images[i])
        st.markdown(project_links[i])