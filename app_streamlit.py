import json
import os
import streamlit as st
from contextual import ContextualAI
from dotenv import load_dotenv

st.set_page_config(page_title="DATABiQ AI Assistant", page_icon="🤖")

st.title("🤖 DATABiQ Knowledge Assistant")
st.write("Consulta el conocimiento empresarial indexado.")

load_dotenv()
api_key = os.getenv("CONTEXTUAL_API_KEY")

if not api_key:
    st.error("No se encontró CONTEXTUAL_API_KEY")
    st.stop()

contextual = ContextualAI(api_key=api_key)

# Cargar configuración
if not os.path.exists("config.json"):
    st.error("No existe config.json. Ejecuta primero ingest_documents.py")
    st.stop()

with open("config.json") as f:
    config = json.load(f)

agent_id = config["agent_id"]

pregunta = st.text_input("Haz una pregunta")

if st.button("Consultar") and pregunta:

    with st.spinner("Consultando base de conocimiento..."):

        response = contextual.agents.query.create(
            agent_id=agent_id,
            messages=[
                {
                    "role": "user",
                    "content": pregunta
                }
            ]
        )

        try:
            respuesta = response.message.content

            st.subheader("Respuesta")
            st.write(respuesta)

        except Exception:
            st.error("No se pudo procesar la respuesta.")