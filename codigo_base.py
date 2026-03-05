# Codigo Base
from contextual import ContextualAI  

contextual = ContextualAI(api_key="xxxxxxx")

#Crear contenedor de conocimiento
datastore = contextual.datastores.create(name="Repositorio Corporativo")
datastore_id = datastore.id

# Inyeccion de Documento Corporativo
with open("Perfil_DATABiQ.pdf", "rb") as f:
    ingestion = contextual.datastores.documents.ingest(datastore_id=datastore_id, file=f)
    print(f"Documento Indexado con ID: {ingestion.id}")

# Creacion de Agente Contextual
agent = contextual.agents.create(
    name="Auditor Corporativo", 
    description="Agente basado en modelo contextual",
    datastore_ids=[datastore_id])

# Interaccion con el Agente Contextual
response = contextual.agents.query.create(
    agent_id=agent.id, 
    messages=[{"role": "user", "content": "¿Cuáles son los servicios prestados por DATABiQ?"}]
)