import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

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
    st.write(
        "La reconexión magnética es un proceso importante en la interacción entre el viento solar y el campo magnético de la Tierra.")
    st.header("Cómo afecta la reconexión magnética")
    st.write(
        "La reconexión magnética puede tener un impacto en la calidad de servicios generados por medio de campos electromagnéticos")
    # Botón
    if st.button("¡Celebremos!"):
        st.balloons()

# Función para la página de información (Opción 2)
def Datos():
    st.title("Información sobre Reconexión Magnética")
    # Agrega más contenido informativo aquí si lo deseas

    # Agregar un botón para ejecutar el código
    if st.button("Ejecutar Análisis de Datos"):
        #fig = analyze_  data()  # Llama a la función de análisis y obtén la figura

        # Muestra la figura en Streamlit
        #st.pyplot(fig)

# Función para analizar los datos
def analyze_data():
    headers = ['year', 'day', 'hour', 'B_scalar', 'Bz_GSM', 'Bz_GSE', 'SW_temperature', 'SW_proton_density',
               'Plasma_Speed', 'Flow_pressure']
    df = pd.read_csv('data1.txt', delim_whitespace=' ', names=headers)
    # En este punto, puedes continuar con el código que proporcionaste para el análisis de datos.
    # Asegúrate de que el código esté dentro de esta función.
    df.max()
    max_values = [9999, 999, 99, 99, 99, 99, 9999999.00, 999.90, 9999.00, 99.99]
    df_raw = df[(df != max_values).all(axis=1)]
    df_raw = df_raw.reset_index(drop=True)
    data_to_find = df_raw['Bz_GSM']
    peaks = sp.signal.find_peaks(data_to_find, height=3.88, distance=20)
    # Mostrar la cantidad de picos en Streamlit
    st.text(f"Los Datos Anomalos son: {len(peaks[0])}")


    # Crear una figura para la gráfica
    fig, ax = plt.subplots()
    ax.plot(data_to_find)
    ax.plot(peaks[0], data_to_find[peaks[0]], "o")

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
