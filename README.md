Seminario de Actualización · 2026
Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial · IFTS N.º 18

Portfolio académico de Lucas Mateo Suárez Ramos, organizado en clases, prácticas y proyectos integradores. Este repositorio reúne trabajos realizados durante la cursada y documenta el uso de Python, herramientas de ciencia de datos, modelos de inteligencia artificial, interfaces web, APIs y despliegue de aplicaciones.

El objetivo es conservar el código y los entregables de cada etapa, mostrar las aplicaciones desarrolladas y facilitar la revisión de los procesos de trabajo.
Proyecto destacado · Trabajo Práctico Final Integrador
DiabeTrack · Estimación de progresión de diabetes
Aplicación web académica que utiliza un modelo de regresión lineal para estimar un indicador de progresión de diabetes a un año a partir de tres variables de entrada: edad, índice de masa corporal (BMI) y presión arterial media (BP).

El proyecto integra el ciclo de desarrollo de una solución de Machine Learning: selección y preparación de datos, entrenamiento del modelo con scikit-learn, evaluación, serialización con Joblib, construcción de una API con FastAPI y conexión con un frontend propio desarrollado con HTML, CSS y JavaScript.
Componente	Acceso
Aplicación web	Abrir DiabeTrack
API	Abrir backend en Render
Documentación interactiva	Swagger / OpenAPI (/docs)
Estado del servicio	Endpoint GET /health
Repositorio	portfolio-seminario en GitHub


Resumen técnico: dataset Diabetes de scikit-learn · variables age, bmi y bp · regresión lineal · modelo serializado en formato .joblib · API REST con FastAPI y validación mediante Pydantic.

Evaluación documentada del modelo: MSE aproximado de 3756,84 y R² aproximado de 0,2909. El resultado refleja una capacidad explicativa moderada con las tres variables seleccionadas; no debe interpretarse como una herramienta de diagnóstico médico.
Proyecto académico y experimental. La predicción es una estimación basada en el modelo entrenado y no reemplaza una evaluación profesional de salud. El servicio backend utiliza un plan gratuito de Render, por lo que puede tardar en responder después de períodos de inactividad.

Recorrido de aprendizaje
El repositorio contiene carpetas de clases y proyectos. El índice siguiente enlaza las carpetas que aparecen en la estructura del repositorio.
Etapa	Tema	Material / entregables
[Clase 2](Clase_02/)	Preparación del entorno y primeros pasos con Git	Configuración del entorno de desarrollo, Python y control de versiones
[Clase 3](Clase_03/)	Git y control de versiones	Trabajo con repositorios, seguimiento de cambios y operaciones habituales de Git
[Clase 4](Clase_04/)	Interfaces con Gradio	Desarrollo de interfaces interactivas para ejecutar funciones de Python
[Clase 5](Clase_05/)	Aplicaciones y despliegue	Publicación de aplicaciones, uso de Streamlit y documentación con Markdown
[Trabajo Práctico Integrador](TP_Integrador/)	Procesamiento y clasificación de textos	Aplicación de técnicas de IA para clasificación de mensajes y evaluación de resultados
Trabajo Práctico Final Integrador	DiabeTrack: modelo propio, API y frontend	Entrenamiento con scikit-learn, serialización del modelo, FastAPI, validación, CORS e integración web


La tabla describe el material identificado en el repositorio y los proyectos trabajados. No implica que todas las clases del programa tengan una carpeta o entrega publicada.
Aplicaciones y servicios publicados
Proyecto / componente	Plataforma	Enlace
DiabeTrack – frontend	GitHub Pages	Abrir aplicación
DiabeTrack – backend	Render	Abrir API
DiabeTrack – documentación	FastAPI / Swagger	Consultar /docs
DiabeTrack – health check	FastAPI	Consultar /health


Los servicios publicados se incluyen como demostración de los desarrollos realizados. La disponibilidad puede variar según el estado de las plataformas de alojamiento y sus planes gratuitos.
Herramientas, tecnologías y conceptos
- Programación y datos: Python, pandas, scikit-learn y Joblib.
- Machine Learning: preparación de datos, entrenamiento, regresión, clasificación y evaluación de modelos.
- Interfaces web: Gradio, Streamlit, HTML, CSS y JavaScript.
- Backend y APIs: FastAPI, Flask, Pydantic, Uvicorn, API REST y JSON.
- Comunicación web: HTTP, métodos GET y POST, códigos de estado, encabezados, fetch() y CORS.
- Pruebas de APIs: navegador, curl / curl.exe y clientes Python con urllib.
- Publicación: Hugging Face Spaces, Render y GitHub Pages.
- Control de versiones y documentación: Git, GitHub, GitHub Codespaces, Markdown y archivos README.md.
- Entornos y dependencias: venv, pip y requirements.txt.
Arquitectura trabajada: del frontend a la API
En las actividades de desarrollo web se trabajó la separación de responsabilidades entre las partes de una aplicación:
- Frontend: interfaz que utiliza la persona, construida con HTML, CSS y JavaScript.
- Backend: lógica que procesa las solicitudes y administra los datos.
- API: contrato de comunicación entre el cliente y el backend.
- HTTP: protocolo utilizado para enviar solicitudes y recibir respuestas.
- JSON: formato de intercambio de datos entre aplicaciones.
- CORS: mecanismo del navegador para controlar solicitudes entre orígenes diferentes.
También se estudiaron distintas formas de implementar una API en Python:
Alternativa	Características principales
Python plano	Implementación manual de rutas, métodos HTTP, encabezados, lectura del cuerpo y respuestas
Flask	Framework con rutas mediante decoradores y utilidades como request.get_json() y jsonify()
FastAPI	Framework con validación de datos mediante Pydantic y documentación automática en /docs


En el proyecto DiabeTrack se aplicó FastAPI para exponer los endpoints del modelo y permitir que el frontend enviara los datos mediante solicitudes HTTP.
Cómo utilizar el repositorio
1. Ingresar a la carpeta de la clase o del proyecto que se quiera revisar.
2. Consultar los archivos de código y la documentación disponibles en esa carpeta.
3. Para ejecutar una actividad localmente, revisar primero sus dependencias y crear un entorno virtual cuando corresponda.
4. Instalar los paquetes indicados en el requirements.txt de la actividad.
5. Seguir las instrucciones específicas de ejecución de cada proyecto.
Ejecución local de DiabeTrack
El backend se ejecuta desde su carpeta correspondiente con Uvicorn:
python -m uvicorn main:app --reload
El frontend puede servirse localmente con el servidor HTTP de Python:
python -m http.server 5500
Las rutas de trabajo dependen de la ubicación de cada carpeta dentro del repositorio. Consultar los archivos del proyecto antes de ejecutar los comandos.
Organización y buenas prácticas
- Mantener cada clase y proyecto en su carpeta correspondiente.
- Documentar objetivos, tecnologías, dependencias y pasos de ejecución.
- Utilizar Git para registrar cambios y GitHub para mantener el repositorio actualizado.
- No publicar claves, tokens, contraseñas ni archivos .env.
- No subir entornos virtuales ni archivos temporales.
- Cargar modelos serializados únicamente desde fuentes confiables.
- Diferenciar los resultados experimentales de las soluciones validadas para uso real.
Transparencia académica
Se utilizaron herramientas de IA generativa como apoyo durante distintas etapas de aprendizaje, por ejemplo para explorar alternativas, comprender conceptos, revisar código, investigar errores y mejorar la documentación. Los desarrollos, pruebas y resultados se documentan en las carpetas y archivos correspondientes del repositorio.
Lucas Mateo Suárez Ramos · Seminario de Actualización · IFTS N.º 18 · 2026
