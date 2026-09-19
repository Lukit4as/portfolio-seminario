# Clase 4 - Del repositorio local al Space

## Tema de la clase

En esta clase trabajamos sobre el proceso de llevar una aplicación desarrollada localmente a una plataforma de publicación.

El objetivo fue comprender cómo una aplicación puede mantenerse versionada mediante Git y GitHub y posteriormente ser publicada para que pueda ejecutarse de forma remota.

## Contenidos

Durante la clase se trabajaron los siguientes temas:

- Hugging Face Spaces
- Configuración de Spaces
- Gradio Spaces SDK
- Settings de un Space
- API Endpoints
- Access Tokens
- Gradio Quickstart
- Gradio Interface
- Gradio Blocks
- Event Listeners
- Uso de `button.click()`
- Git `remote`
- Git `pull`
- Git `merge`
- Resolución de conflictos

## Trabajo realizado

Como parte de la práctica, se continuó trabajando con la aplicación desarrollada anteriormente.

La aplicación fue adaptada utilizando Gradio y posteriormente se trabajó con la estructura de `Blocks`, utilizando componentes como:

- `gr.Markdown`
- `gr.Textbox`
- `gr.Button`

También se implementó un evento mediante `button.click()` para ejecutar una función al presionar el botón.

## Aplicación desarrollada

La aplicación permite ingresar un nombre y, al presionar el botón "Saludar", genera un mensaje personalizado.

La estructura utilizada fue:

- Una función de Python para generar el mensaje.
- Un campo de texto para ingresar el nombre.
- Un botón para ejecutar la función.
- Un campo de texto para mostrar el resultado.

## Git y GitHub

Los cambios realizados en la aplicación fueron registrados mediante Git y enviados al repositorio de GitHub.

Se utilizó el flujo:

1. Modificar el código.
2. Verificar los cambios con `git status`.
3. Preparar los cambios con `git add`.
4. Crear un commit con `git commit`.
5. Subir los cambios a GitHub mediante `git push`.

## Resultado

La aplicación fue ejecutada correctamente desde GitHub Codespaces utilizando Gradio.

También se practicó la utilización de `Blocks` y eventos para construir una interfaz interactiva.

## Tecnologías utilizadas

- Python
- Gradio
- Git
- GitHub
- GitHub Codespaces