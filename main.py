import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import requests
import numpy as np

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
    st.write("""La reconexión magnética es un proceso en el que las líneas de campo magnético de diferentes dominios magnéticos se rompen, se vuelven a conectar y crean nuevas configuraciones. En este fenómeno, las líneas de campo magnético se aproximan entre sí y se vuelven antiparalelas; las fuerzas de tensión magnética impiden la colisión inmediata y conducen a la formación de una fina capa de corriente denominada "región de difusión". En la región de difusión, las líneas de campo magnético se rompen y vuelven a conectarse, y el proceso libera energía magnética, convirtiéndola en energía cinética y calor. Comprender la reconexión magnética es crucial para estudiar la física solar y espacial, así como para predecir y mitigar los impactos de los fenómenos meteorológicos espaciales en sistemas tecnológicos como los satélites y las redes eléctricas.""")
    st.header("Cómo afecta la reconexión magnética")
    st.write(
        "")
    st.write("""La reconexión magnética puede tener varios efectos en los satélites y sistemas espaciales. Éstas son algunas de las formas en que puede afectarles:""")
    # URL del video de YouTube
    video_url = "https://www.youtube.com/watch?v=mgUZwoR0gcE"

    # Mostrar el video de YouTube en la interfaz
    st.video(video_url)
    # Botón
    st.button("¡1.- Daño a los sistemas satelitales!") 
    st.button("¡2.- Perturbaciones en la propagación de las ondas de radio!")
    st.button("¡3.- Cambio en la órbita de los satélites")
    st.button("¡4.-  Errores de navegación")
    st.button("¡5.-  Tormentas geomagnéticas")
        

# Función para la página de información (Opción 2)
def Datos():
    st.title("Información sobre Reconexión Magnética")
    # Agrega más contenido informativo aquí si lo deseas

    # Agregar un botón para ejecutar el código
    if st.button("Ejecutar Análisis de Datos"):
        fig = analyze_data()  # Llama a la función de análisis y obtén la figura

        # Muestra la figura en Streamlit
        st.pyplot(fig)

# Función para analizar los datos
def analyze_data():
    url="https://danielperez.pythonanywhere.com/get_past_peeks/"
    resp = requests.get(url)
    
    df = pd.DataFrame(resp.json()["DataFrame"].values(),index=resp.json()["DataFrame"].keys())
    
    time = np.array(resp.json()['time'])
    lista = np.array(df)
    value = np.array(lista[time])


    # Crear una figura para la gráfica
    fig, ax = plt.subplots()
    ax.plot(lista)
    ax.plot(time, value, "o")

    return fig  # Devuelve la figura

# Función para la página de contacto (Opción 3)
def pagina_contacto():
    st.title("Contáctenos")
    st.write("Si tienes preguntas o comentarios, no dudes en ponerte en contacto con nosotros.")

    # Crea 6 columnas
    Uno_col, Dos_col, Tres_col, Cuatro_col, Cinco_col, Seis_col = st.columns(6)

    with Uno_col:
        st.image("1.png", width=110)
        st.markdown("**Nombre:** Angelica")
        st.markdown("**Apellido:** Escobedo")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

    with Dos_col:
        st.image("2.png", width=110)
        st.markdown("**Nombre:**  Gabriel")
        st.markdown("**Apellido:** Barajas")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

    with Tres_col:
        st.image("3.png", width=110)
        st.markdown("**Nombre:** Daniel")
        st.markdown("**Apellido:** Salgado")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

    with Cuatro_col:
        st.image("4.png", width=110)
        st.markdown("**Nombre:** Mauricio")
        st.markdown("**Apellido:** Lopez")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

    with Cinco_col:
        st.image("5.png", width=110)
        st.markdown("**Nombre:** Francisco")
        st.markdown("**Apellido:** Moreno")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

    with Seis_col:
        st.image("6.png", width=110)
        st.markdown("**Nombre:** Vicente")
        st.markdown("**Apellido:** Montero")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)


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
