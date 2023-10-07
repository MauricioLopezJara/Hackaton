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
    st.write("☆ La calidad de Servicios")
    st.write("☆ Sistemas de navegacion")
    st.write("☆ Las comunicaciones")
    st.write("☆ Daña sistemas electronicas de naves espaciales")

# Función para la página de información (Opción 2)
def Datos():
    st.title("Información sobre Reconexión Magnética")
    # Agrega más contenido informativo aquí si lo deseas

# Función para la página de contacto (Opción 3)
def pagina_contacto():
  st.title("Contáctenos")
  st.write("Si tienes preguntas o comentarios, no dudes en ponerte en contacto con nosotros.")
  
 # Formulario de contacto
  with st.form("formulario_contacto"):
    nombre = st.text_input("Nombre", required=True)
    correo = st.text_input("Correo Electrónico", required=True)
    mensaje = st.text_area("Mensaje", required=True)
    enviar = st.form_submit_button("Enviar")
  # Agrega información de contacto si lo deseas


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

