import gradio as gr
import os

def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido a mi portfolio de Seminario."


with gr.Blocks() as app:
    gr.Markdown("# Mi primera aplicación con Gradio")
    gr.Markdown("Una aplicación sencilla desarrollada para Seminario.")

    nombre = gr.Textbox(label="Tu nombre")
    boton = gr.Button("Saludar")
    mensaje = gr.Textbox(label="Mensaje")

    boton.click(
        fn=saludar,
        inputs=nombre,
        outputs=mensaje
    )


app.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))