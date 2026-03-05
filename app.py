from contextual import ContextualAI
from dotenv import load_dotenv
import os
import time

print("\nInicializando sistema RAG...\n")

# -------------------------
# Cargar variables de entorno
# -------------------------

load_dotenv()

api_key = os.getenv("CONTEXTUAL_API_KEY")

if not api_key:
    raise ValueError("No se encontró la API KEY en el archivo .env")

contextual = ContextualAI(api_key=api_key)

# -------------------------
# Crear datastore
# -------------------------

print("Creando datastore nuevo...")

datastore = contextual.datastores.create(
    name="Repositorio_DATABiQ"
)

datastore_id = datastore.id

print(f"Datastore creado: {datastore_id}\n")

# -------------------------
# Ingestar documento
# -------------------------

print("Subiendo documento...")

with open("Perfil_DATABiQ.pdf", "rb") as f:
    ingestion = contextual.datastores.documents.ingest(
        datastore_id=datastore_id,
        file=f
    )

print(f"Documento cargado: {ingestion.id}\n")

# Esperar indexación
print("Procesando documento para indexación...")
time.sleep(15)

print("Indexación completada.\n")

# -------------------------
# Crear agente
# -------------------------

print("Creando agente RAG...")

agent = contextual.agents.create(
    name="Auditor_DATABiQ",
    description="Agente RAG para consultas empresariales",
    datastore_ids=[datastore_id]
)

agent_id = agent.id

print(f"Agente creado: {agent_id}\n")

print("Sistema listo para consultas.")
print("Escribe 'salir' para terminar.\n")

# -------------------------
# Loop interactivo
# -------------------------

while True:

    pregunta = input("Pregunta: ")

    if pregunta.lower() == "salir":
        print("\nSesión finalizada.")
        break

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
        print("\nRespuesta:\n")
        print(respuesta)
        print("\n------------------------------------\n")

    except Exception:
        print("\nNo se pudo interpretar la respuesta.\n")