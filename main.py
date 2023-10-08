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


# Función para la página de contacto (Opción 3)
def pagina_contacto():
    st.title("Contáctenos")
    st.write("Si tienes preguntas o comentarios, no dudes en ponerte en contacto con nosotros.")
    
    # Crea 6 columnas
    Uno_col, Dos_col, Tres_col, Cuatro_col, Cinco_col, Seis_col = st.columns(6)

    with Uno_col:
        st.image("1.png", width=110)
        st.markdown("**Nombre:** Juan Pérez")
        st.markdown("**Cargo:** Desarrollador web")
        st.markdown(f'<a href=http://www.facebook.com>"link"<\a>', unsafe_allow_html=True)

    with Dos_col:
        st.image("2.png", width=110)
        st.markdown("**Nombre:** María López")
        st.markdown("**Cargo:** Diseñadora gráfica")

    with Tres_col:
        st.image("3.png", width=110)
        st.markdown("**Nombre:** Juan Pérez")
        st.markdown("**Cargo:** Desarrollador web")

    with Cuatro_col:
        st.image("4.png", width=110)
        st.markdown("**Nombre:** María López")
        st.markdown("**Cargo:** Diseñadora gráfica")

    with Cinco_col:
        st.image("5.png", width=110)
        st.markdown("**Nombre:** Juan Pérez")
        st.markdown("**Cargo:** Desarrollador web")

    with Seis_col:
        st.image("6.png", width=110)
        st.markdown("**Nombre:** María López")
        st.markdown("**Cargo:** Diseñadora gráfica")
    # Muestra la imagen en la columna central de la función de contacto
    #Uno_col.image("1.png", width=110)
    
    #Dos_col.image("2.png", width=110)
    
    #Tres_col.image("3.png", width=110)
    
    #Cuatro_col.image("4.png", width=110)
    
    #Cinco_col.image("5.png", width=110)
    
    #Seis_col.image("6.png", width=110)
    
    
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
