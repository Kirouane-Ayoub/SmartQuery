from dotenv import load_dotenv
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_cohere import CohereRerank
from langchain_community.document_loaders import PyPDFDirectoryLoader

from chains.models import Cohere_embeddings
from retrievers.query_generator import query_generator

load_dotenv()

INPUT_DATA_FOLDER = "data_input"

print("--------- Loading Data -----------------")
loader = PyPDFDirectoryLoader(INPUT_DATA_FOLDER)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1800, chunk_overlap=200)
chunks = text_splitter.split_documents(docs)
print("----------Create base retriver-----------------")

db = Chroma.from_documents(chunks, Cohere_embeddings)
base_retriever = db.as_retriever()

print("----------Create multi query Retriever-----------------")

multi_query_retriever = MultiQueryRetriever(
    retriever=base_retriever,
    llm_chain=query_generator,
    parser_key="lines",
    verbose=True,
)

print("----------Create CohereRerank-----------------")

compressor = CohereRerank()
print("----------Create compression retriever-----------------")

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=multi_query_retriever
)
