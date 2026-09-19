# Clase 5 - Deploy y documentación

## Actividad: Publicá tu app y documentala

En esta actividad se publicó la aplicación desarrollada con Gradio Blocks en un servidor real y se realizó una versión equivalente utilizando Streamlit.

El objetivo fue comprobar que el procedimiento de publicación no depende de una única herramienta para construir la interfaz.

## 1. Deploy en Render

La primera versión de la aplicación utiliza **Gradio Blocks**.

La aplicación permite ingresar un nombre y, al presionar el botón "Saludar", muestra un mensaje personalizado.

### Tecnologías utilizadas

- Python
- Gradio
- Git
- GitHub
- Render

### Link del deploy

https://portfolio-seminario.onrender.com

El deploy se realizó utilizando un Web Service de Render conectado al repositorio de GitHub.

Se configuró:

- Root Directory: `Clase_04`
- Build Command: `pip install -r requirements.txt`
- Start Command: `python app.py`

El deploy finalizó correctamente y la aplicación quedó disponible online.

## 2. Versión equivalente en Streamlit

Para comprobar que el procedimiento no dependiera de Gradio, se desarrolló una versión equivalente de la aplicación utilizando **Streamlit**.

Esta versión mantiene la misma idea principal:

1. Ingresar un nombre.
2. Presionar el botón "Saludar".
3. Mostrar un mensaje personalizado.

### Tecnologías utilizadas

- Python
- Streamlit
- Git
- GitHub
- Streamlit Community Cloud

### Link del deploy

https://portfolio-seminario-lfn95sjdcfnvjsphwy9xu8.streamlit.app/

## 3. Diferencias entre las dos versiones

Las dos aplicaciones realizan la misma función, pero utilizan herramientas diferentes para construir la interfaz.

### Gradio

En la versión con Gradio se utilizó `gr.Blocks()` para construir la interfaz y `button.click()` para ejecutar la función cuando se presiona el botón.

### Streamlit

En la versión con Streamlit se utilizaron elementos como:

- `st.title()`
- `st.write()`
- `st.text_input()`
- `st.button()`

La lógica general de la aplicación se mantiene, pero cambia la forma de construir la interfaz y gestionar la interacción.

## 4. Comparación del deploy

Las dos aplicaciones fueron publicadas correctamente.

- **Render:** aplicación desarrollada con Gradio Blocks.
- **Streamlit Community Cloud:** versión equivalente desarrollada con Streamlit.

El resultado permitió comprobar que una aplicación sencilla puede ser publicada utilizando diferentes herramientas y plataformas.

## 5. Documentación

Durante la actividad también se trabajó con archivos `README.md` y Markdown para documentar el proyecto y facilitar la comprensión de su estructura, tecnologías y formas de acceso.

## Resultado final

Se obtuvieron dos aplicaciones funcionando online:

### Gradio + Render

https://portfolio-seminario.onrender.com

### Streamlit

https://portfolio-seminario-lfn95sjdcfnvjsphwy9xu8.streamlit.app/