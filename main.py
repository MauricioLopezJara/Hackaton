import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="NASA Reconexión Magnética",
    page_icon="🌌",
    layout="centered"
)

# Función para la página de bienvenida
def pagina_bienvenida():
    # Crea 3 columnas
    left_col, mid_col, right_col = st.columns(3)

    # Muestra la imagen en la columna central
    mid_col.image("Nasa.png", width=200)
    st.title("Bienvenido a la página de la NASA sobre la Reconexión Magnética de la Tierra")
    st.write("La reconexión magnética es un proceso importante en la interacción entre el viento solar y el campo magnético de la Tierra.")
    st.header("Cómo afecta la reconeccion magnetica")
    st.write("La reconexión magnética puede tener un impacto en la calidad de servicios generados por medio de campos electromagneticos")
    # Botón
    if st.button("¡Celebremos!"):
        st.balloons()


# Función para la página de información (Opción 2)
def Datos():
    st.title("Información sobre Reconexión Magnética")
    # Agrega más contenido informativo aquí si lo deseas


def pagina_contacto():
    st.title("Contáctenos")
    st.write("Si tienes preguntas o comentarios, no dudes en ponerte en contacto con nosotros.")

    # Crea 3 columnas
    Uno_col, Dos_col, Tres_col, Cuatro_col, Cinco_col, Seis_col = st.columns(6)

    # Crea enlaces a perfiles de LinkedIn
    linkedin_links = {
        "1.png": "https://linkedin.com/in/perfil-1",
        "2.png": "https://linkedin.com/in/perfil-2",
        "3.png": "https://linkedin.com/in/perfil-3",
        "4.png": "https://linkedin.com/in/perfil-4",
        "5.png": "https://linkedin.com/in/perfil-5",
        "6.png": "https://linkedin.com/in/perfil-6",
    }

    # Muestra las imágenes como enlaces a perfiles de LinkedIn
    for img_filename, linkedin_link in linkedin_links.items():
        with Uno_col:
            st.markdown(f'<a href="{linkedin_link}" target="_blank"><img src="{img_filename}" width="110"></a>', unsafe_allow_html=True)

# Título del menú
st.sidebar.markdown("Bienvenido al Menu")

# Elementos del menú
opciones = ["Bienvenida", "Datos", "Contacto"]
eleccion = st.sidebar.selectbox("Selecciona una opción:", opciones)

# Contenido de la página según la elección
if eleccion == "Bienvenida":
    pagina_bienvenida()
elif eleccion == "Datos":
    Datos()
elif eleccion == "Contacto":
    pagina_contacto()
