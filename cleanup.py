from contextual import ContextualAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CONTEXTUAL_API_KEY")

contextual = ContextualAI(api_key=api_key)

datastores = contextual.datastores.list()

for ds in datastores:

    print(f"Eliminando datastore: {ds.name}")

    contextual.datastores.delete(ds.id)