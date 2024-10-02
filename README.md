# Proyecto de Control de Arduino y Uso de Roles en Ollama

Este repositorio incluye dos pruebas realizadas de código en Python, una para interactuar con un **Arduino** y con la herramienta de NLP **Spacy**, la otra para usar **Ollama** una herramienta (ejecutable en local) que permite interactuar con LLM a través de una API.

## Scripts incluidos

1. **Control de LED con Arduino**:
   - NLPcontrolledLED.py es un script Python que en función de si se ingresa una frase positiva o negativa, controlará el encendido o apagado de un LED conectado a un Arduino.
   - Spacy se encarga de hacer el sentiment analysis para valorar la emoción de la frase.
   - Al mismo tiempo se tiene que ejecutar sketch_pyserial.ino en el Arduino, que estará conectado por puerto serial al ordenador (o de otra manera).
   - Frases positivas -> LED encendido.
   - Frases negativas -> LED apagado.

2. **Interacción con Ollama en Jupyter Notebook**:
   - Un Jupyter Notebook que permite interactuar con **Ollama**, utilizando diferentes roles en los mensajes para simular respuestas de varios perfiles o personajes.
   - Ideal para explorar y probar distintos enfoques de conversación en un entorno interactivo.
   - Esto nos permitirá poderlo incluir en otras apliaciones en que podamos aprovechar un LLM (Juegos de Rol o Interacción Narrativa, Chatbots para Atención al Cliente,Resumen de Documentos, etc)

