import streamlit as st

st.title("Mi primera aplicación con Streamlit")

st.write("Una aplicación sencilla desarrollada para Seminario.")

nombre = st.text_input("Tu nombre")

if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}! Bienvenido a mi portfolio de Seminario.")