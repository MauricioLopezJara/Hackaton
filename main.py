import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="NASA Reconexión Magnética",
    page_icon="🌌",
    layout="centered"
)

# Función para la página de bienvenida
def pagina_contacto():
  st.title("Contáctenos")
  st.write("Si tienes preguntas o comentarios, no dudes en ponerte en contacto con nosotros.")
  
  # Formulario de contacto
  with st.form("formulario_contacto"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo Electrónico")
    mensaje = st.text_area("Mensaje")
    enviar = st.form_submit_button("Enviar")
    
  if enviar:
    # Validación de campos obligatorios
    if not nombre or not correo or not mensaje:
      st.warning("Por favor, completa todos los campos obligatorios.")
    else:
      # Procesamiento del formulario aquí
      # Por ejemplo, puedes almacenar los datos en una base de datos
      st.success(f"Gracias por contactarnos, {nombre}! Hemos recibido tu mensaje.")
      # Agrega un botón para volver a la página de bienvenida
      st.button("Volver a la página de bienvenida", on_click=pagina_bienvenida)


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
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo Electrónico")
    mensaje = st.text_area("Mensaje")
    enviar = st.form_submit_button("Enviar")

  if enviar:
    # Validación de campos obligatorios
    if not nombre or not correo or not mensaje:
      st.warning("Por favor, completa todos los campos obligatorios.")
    else:
      # Procesamiento del formulario aquí
      # Por ahora, simplemente mostraremos un mensaje de confirmación.
      st.success(f"Gracias por contactarnos, {nombre}! Hemos recibido tu mensaje.")
        



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

