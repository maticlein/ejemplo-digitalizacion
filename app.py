import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():

    favicon = Image.open('./img/logo_innovacion.png')

    st.set_page_config(
        page_title = 'Ejemplo de muestreo',
        page_icon = favicon,
        layout = 'centered',
        initial_sidebar_state = 'expanded'
    )

    logo = Image.open('./img/logo_ufro_innovacion.png')
    st.image(logo, width = 200)    
    st.title('Taller de Diseño de Ingeniería')
    st.header('Ejemplo de Muestreo')

    st.sidebar.title('Parámetros')
    f = st.sidebar.slider(label = 'Frecuencia Señal Original', min_value = 1, max_value = 50)
    fs = st.sidebar.slider(label = 'Frecuencia de Muestreo', min_value = 1, max_value = 1000)
    niveles_cuantizacion = st.sidebar.slider(label = 'Niveles de Cuantización', min_value = 1, max_value = 100)

    col1, col2, col3 = st.columns(3)

    col1.metric('Frecuencia Señal Original', f)
    col2.metric('Frecuencia de Muestreo', fs)
    col3.metric('Niveles de Cuantización', niveles_cuantizacion)

    w = 2 * np.pi * f
    x = np.arange(0, 1.01, 0.00001)
    y = (np.sin(w * x) + 1) / 2

    ts = 1 / fs
    x_2 = np.arange(0, 1.01, ts)
    y_2 = (np.sin(w * x_2) + 1) / 2

    plt.plot(x, y)
    plt.plot(x_2, y_2, '*')
    plt.xlim(0, 0.2)
    plt.ylim(0, 1)

    lineas_muestreo = st.checkbox('Lineas de Muestreo')
    if lineas_muestreo:
        for i in range(0, len(x_2) - 1):
            plt.axhline(y_2[i], x_2[i] / 0.2, x_2[i + 1] / 0.2, c = 'r')
            plt.axvline(x_2[i + 1], y_2[i], y_2[i + 1], c = 'r')

    lineas_niveles_cuantizacion = st.checkbox('Niveles de Cuantización')
    if lineas_niveles_cuantizacion:
        for i in np.arange(0, 1, 1 / niveles_cuantizacion):
            plt.axhline(i, c = 'g')

    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    st.pyplot(fig = plt)

if __name__ == '__main__':
    main()