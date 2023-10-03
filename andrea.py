import streamlit as st
import pandas as pd
import streamlit_option_menu
from streamlit_option_menu import option_menu
from PIL import Image
import psycopg2
from datetime import datetime
import random
import requests
import json
import os

API_ENDPOINT = os.environ.get("API_ENDPOINT", "http://localhost:8080")


#prediccion
def call_api_predict_method(link):
    request_data = [{
        "link": link,
                    }]
    
    request_data_json = json.dumps(request_data)
    headers = {
    'Content-Type': 'application/json'
                }
    predict_method_endpoint = f"{API_ENDPOINT}/iris/predict"
    response = requests.request("POST",predict_method_endpoint , headers=headers, data=request_data_json)
    response_json = response.json()
    predictions = response_json['predictions']
    label = predictions[0]
    return label

#estructura inicial de la app
def estructure():
    
    st.set_page_config(page_title="Andrea App",page_icon="🧊")
    
    # Título de la aplicación
    st.markdown("<h1 style='text-align: center;'>ENLACE FACIL</h1>", unsafe_allow_html=True)
    st.sidebar.image("andrea.gif")
    
        # Informacion del modelo
    with st.sidebar:
        selected = option_menu(
        menu_title = "Control del Modelo",
        options = ["Modelo"],
        icons = ["book"],
        menu_icon = "cloud",
        default_index = 0,)

    # codigo para el MODELO 
    if selected=="Modelo":
        
        st.sidebar.subheader("Descripción del Modelo")
        #meticas y como se realizo el modelo 1
        st.sidebar.write("Aquí puedes escribir la descripción del Modelo.")
        
     # Crear pestañas
    tabs = st.tabs(["APPY", "BIBILOTECA",])

    return(tabs)

#clasificacion usando el modelo
def LinkScribe(tabs):
    label=[]
    # Contenido de la pestaña "APPY"
    with tabs[0]:
        
        # Título de la subpágina
        st.markdown("<h1 style='text-align:;'>LinkScribe</h1>", unsafe_allow_html=True)
        
        # Entrada de enlace
        link = st.text_input("Ingresa un enlace:", "")
        submit_button = st.button("Procesar Enlace")

        #verificamos que sea un link correcto
        if submit_button:
            if link:
                
                label=call_api_predict_method(link)
                label=1
                # Cuadro de Información del Enlace
                st.subheader("Título de la paguina:")
                st.write(link)
                st.subheader("Descripción:")
                st.write(link)  
                st.subheader("imagen de vista previa:")
                st.write(link)           
                st.subheader("LINK:")
                st.write(link) 
                st.subheader("Categoria:",)  

            # Aquí puedes agregar la lógica para procesar el enlace después de hacer clic en el botón
            else:
                # Mensaje de error  ingresó una URL
                st.markdown("<p style='color: red;'>Por favor, ingresa una URL.</p>", unsafe_allow_html=True)
    return(label)

#comunicacion con la base de datos
def baseDatos(tabs):
     with tabs[1]:
    # Aquí puedes agregar la lógica y código para mostrar gráficas
        st.title("BASE DE DATOS")

        # Datos simulados (lista de diccionarios)
        datos_simulados = [
            {
                "titulo": "Andrea",
                "descripcion": "Descripción del artículo 1",
                "categoria": "Ficción",
                "fecha_publicacion": "2023-01-15"
            },
            {
                "titulo": "Carlos",
                "descripcion": "Descripción del artículo 2",
                "categoria": "No ficción",
                "fecha_publicacion": "2023-02-20"
            },
            {
                "titulo": "Andres",
                "descripcion": "Descripción del artículo 3",
                "categoria": "Otra categoría",
                "fecha_publicacion": "2023-03-25"
            }
        ]

        # Función para filtrar los datos simulados
        def get_filtered_data(filtro_titulo, filtro_categoria, fecha_inicio):
            data_filtrada = datos_simulados

            if filtro_titulo:
                data_filtrada = [item for item in data_filtrada if filtro_titulo.lower() in item["titulo"].lower()]
            if filtro_categoria != "Todas":
                data_filtrada = [item for item in data_filtrada if item["categoria"] == filtro_categoria]
            if fecha_inicio:
                fecha_inicio_str = fecha_inicio.strftime("%Y-%m-%d")
                data_filtrada = [item for item in data_filtrada if fecha_inicio_str <= item["fecha_publicacion"]]

            return data_filtrada

        # Interfaz de usuario de Streamlit

        filtro_titulo = st.text_input("Buscar por título:", "")
        categorias = ["Todas", "Ficción", "No ficción", "Otra categoría"]
        filtro_categoria = st.selectbox("Filtrar por categoría:", categorias)
        fecha_inicio = st.date_input("Fecha de inicio:")

        data_filtrada = get_filtered_data(filtro_titulo, filtro_categoria, fecha_inicio)

        st.write("Datos simulados:")
        for item in data_filtrada:
            if st.button(f"Ver Descripción de '{item['titulo'], item['categoria']}'"):
                st.subheader("Descripción:")
                st.write(item["descripcion"])
    
#app
def app():
    
    #estructura
    tabs=estructure()
    
    #modelo de predicciones   
    lable=LinkScribe(tabs)

    # Contenido coneccion con base de datos
    baseDatos(tabs)



if __name__ == '__main__':
    app()