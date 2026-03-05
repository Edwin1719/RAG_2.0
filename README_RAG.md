# RAG 2.0 con Contextual AI - Sistema de Inteligencia Empresarial

## 🚀 Descripción General
Este proyecto implementa un sistema de **Generación Aumentada por Recuperación (RAG 2.0)** utilizando la plataforma **Contextual AI**. A diferencia del RAG tradicional, esta técnica utiliza **Contextual Retrieval**, lo que permite una precisión superior al indexar y recuperar información de documentos corporativos complejos (PDF).

El sistema actúa como un "Cerebro Digital" que permite interactuar con el conocimiento de la empresa a través de lenguaje natural.

---

## 🏗️ Arquitectura del Sistema
El proyecto se divide en dos fases críticas para garantizar eficiencia y escalabilidad:

1.  **Fase de Ingesta (`ingest_documents.py`)**: 
    - Crea el Datastore (base de conocimiento).
    - Indexa el documento `Perfil_DATABiQ.pdf` con metadatos contextuales.
    - Configura el Agente de IA y guarda las credenciales en `config.json`.
2.  **Fase de Interacción (Dual)**:
    - **Terminal (`app.py`)**: Interfaz rápida para pruebas y depuración técnica.
    - **Interfaz Web (`app_streamlit.py`)**: Aplicación visual moderna para usuarios finales.

---

## 🛠️ Instalación y Configuración

### 1. Requisitos Previos
- Python 3.10+
- Cuenta en Contextual AI (API Key)

### 2. Configuración del Entorno
```bash
# Crear y activar entorno
conda create -n RAG_NEW python=3.10
conda activate RAG_NEW

# Instalar dependencias
pip install contextual-client python-dotenv streamlit
```

### 3. Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
CONTEXTUAL_API_KEY=tu_api_key_aqui
```

---

## 📂 Flujo de Ejecución

### Paso 1: Ingesta de Conocimiento
Antes de preguntar, debemos "enseñar" al sistema. Este paso solo se ejecuta cuando hay documentos nuevos.
```bash
python ingest_documents.py
```
*Esto generará un archivo `config.json` con los IDs necesarios.*

### Paso 2: Despliegue de la Interfaz
Puedes elegir cómo interactuar con el sistema:

#### Opción A: Interfaz Web (Recomendado)
Para una experiencia visual de chat:
```bash
streamlit run app_streamlit.py
```

#### Opción B: Consola
Para consultas rápidas desde la terminal:
```bash
python app.py
```

---

## 💼 Casos de Uso: Sector de Bienes y Servicios
La tecnología de **Contextual RAG** es un diferenciador competitivo en el sector empresarial. Aquí detallamos cómo aplicarla:

### 1. Gestión de Bienes (Real Estate / Activos fijos)
- **Análisis de Contratos:** Consultar cláusulas específicas, fechas de vencimiento o penalizaciones en contratos de arrendamiento complejos.
- **Fichas Técnicas de Propiedades:** Consultar especificaciones de construcción, materiales y normativas legales de un portafolio inmobiliario.
- **Auditoría de Activos:** Localizar rápidamente garantías y manuales de mantenimiento de maquinaria o infraestructura.

### 2. Sector Servicios (Consultoría / BPO / IT)
- **Asistente de Propuestas (Sales Enablement):** Consultar casos de éxito previos, metodologías de trabajo y perfiles corporativos para armar licitaciones en minutos.
- **Onboarding de Clientes:** Extraer requerimientos críticos de documentos de "SLA" (Acuerdos de Nivel de Servicio).
- **Compliance y Legal:** Verificar si una propuesta cumple con las normativas internas o políticas de privacidad vigentes.

### 3. Atención al Cliente Especializada
- **Soporte de Segundo Nivel:** Proveer a los agentes de soporte una herramienta que "lea" todos los manuales técnicos y responda soluciones precisas a problemas complejos del cliente.
- **Base de Conocimiento Dinámica:** Convertir los FAQs estáticos en un chat inteligente que entiende el contexto del problema del usuario.

---

## 📈 Ventajas Competitivas
- **Cero Alucinaciones:** Las respuestas están ancladas 100% al documento indexado.
- **Privacidad:** Los datos empresariales se procesan en un entorno seguro y controlado.
- **Escalabilidad:** Puede manejar desde un PDF de 10 páginas hasta bibliotecas completas de documentación técnica.

---
*Desarrollado para la optimización de procesos mediante Inteligencia Artificial Generativa.*
