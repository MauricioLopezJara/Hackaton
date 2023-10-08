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
    linkedin_links = [
        {"img":"1.png", "link":"https://theblogmauriciol.wordpress.com","col":Uno_col},
        {"img":"2.png", "link":"https://linkedin.com/in/perfil-2","col":Dos_col},
        {"img":"3.png", "link":"https://linkedin.com/in/perfil-3","col":Tres_col},
        {"img":"4.png", "link":"https://linkedin.com/in/perfil-4","col":Cuatro_col},
        {"img":"5.png", "link":"https://linkedin.com/in/perfil-5","col":Cinco_col},
        {"img":"6.png", "link":"https://linkedin.com/in/perfil-6","col":Seis_col}
    ]

    # Muestra las imágenes como enlaces a perfiles de LinkedIn
    for x in linkedin_links:
            x["col"].markdown(f'<a href="{x["link"]}" target="_blank">{st.image(x["img"], width=110)}<\a>') 

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
