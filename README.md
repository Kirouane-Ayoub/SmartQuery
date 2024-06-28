# SmartQuery 


This project leverages the power of 🦜️🔗 **LangChain** to create an advanced **conversational agent** with sophisticated query retrieval capabilities. We utilize state-of-the-art **embedding models**, vector storage, and **reranking** mechanisms to ensure high-quality responses and interactions.

## Key Components

### Vector Store and Embedding Model

- **Vector Store**: ChromaDB
- **Embedding Model**: `embed-english-v3.0` by Cohere

### Retrieval and Ranking Pipeline

1. **Base Retriever**: Initiates the retrieval process by fetching relevant documents.
2. **Multi Query Retriever**: Enhances the retrieval by generating multiple queries from different perspectives.
3. **CohereRerank**: Reranks the retrieved documents to ensure the most semantically relevant ones are prioritized.
4. **Compression Retriever**: Combines all components to produce a refined set of documents for the conversational agent.

### Language Models

- **Conversational ReAct Agent**: `command-r-plus` by Cohere
- **MultiQueryRetriever**: `claude-3-opus-20240229` by Anthropic

### FastAPI Application

A **FastAPI** app is created using **🦜️🏓 LangServe** to deploy this sophisticated pipeline as a production-ready service.

## Components Description

### REACT AGENT

The **REACT AGENT** is based on the **Reasoning + Action** framework for LLMs. It generates responses at every step through reasoning and takes appropriate actions based on this reasoning. This iterative process ensures that the agent can handle complex queries and provide accurate and contextually relevant responses.

### MultiQueryRetriever

Traditional distance-based vector database retrieval may not always capture the nuances of a query. The **MultiQueryRetriever** addresses this by generating multiple queries from different perspectives using an LLM. This process retrieves a more comprehensive set of relevant documents by considering various angles of the user input, thus enhancing the overall retrieval process.

### CohereRerank

The **CohereRerank** API ranks documents based on their semantic relevance to a given query. This powerful tool ensures that the most contextually appropriate documents are prioritized, improving the accuracy and quality of the responses provided by the agent.

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Kirouane-Ayoub/SmartQuery .git
    cd SmartQuery 
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```
4. **Configure environment variables**:

    Ensure you have the necessary API keys set up in your environment.
    ```bash
    ANTHROPIC_API_KEY=..
    COHERE_API_KEY=..
    ```
6. **Run the server**:

    ```bash
    python server.py
    ```


## Usage

Once the server is running, you can interact with the agent via the provided endpoints. The FastAPI interface allows for easy testing and integration with other services.

![Screenshot from 2024-06-28 02-35-52](https://github.com/Kirouane-Ayoub/SmartQuery-/assets/99510125/4567b30b-394c-4fca-a21e-084a1fcb36a5)
