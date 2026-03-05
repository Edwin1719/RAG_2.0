import json
import os
import time
from contextual import ContextualAI
from dotenv import load_dotenv

print("\nInicializando proceso de ingesta...\n")

load_dotenv()
api_key = os.getenv("CONTEXTUAL_API_KEY")

if not api_key:
    raise ValueError("No se encontró CONTEXTUAL_API_KEY en .env")

contextual = ContextualAI(api_key=api_key)

# Crear datastore
print("Creando datastore...")

datastore = contextual.datastores.create(
    name="Repositorio_DATABiQ"
)

datastore_id = datastore.id

print(f"Datastore creado: {datastore_id}")

# Subir documento
print("\nSubiendo documento...")

with open("Perfil_DATABiQ.pdf", "rb") as f:

    ingestion = contextual.datastores.documents.ingest(
        datastore_id=datastore_id,
        file=f
    )

print(f"Documento cargado: {ingestion.id}")

# Esperar indexación
print("\nIndexando documento...")
time.sleep(15)

# Crear agente
print("\nCreando agente...")

agent = contextual.agents.create(
    name="Auditor_DATABiQ",
    description="Agente RAG para consultas empresariales",
    datastore_ids=[datastore_id]
)

agent_id = agent.id

print(f"Agente creado: {agent_id}")

# Guardar configuración
config = {
    "datastore_id": datastore_id,
    "agent_id": agent_id
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print("\nConfiguración guardada en config.json")
print("\nProceso completado.")