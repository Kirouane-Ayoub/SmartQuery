from dotenv import load_dotenv
from langchain.llms import Cohere
from langchain_anthropic import ChatAnthropic
from langchain_cohere import CohereEmbeddings

from chains import settings

load_dotenv()

Anthropic_model = ChatAnthropic(model=settings.ANTHROPIC_LLM_MODEL)

Cohere_embeddings = CohereEmbeddings(model=settings.COHERE_EMBEDDING_MODEL)

Command = Cohere(model=settings.COHERE_LLM_MODEL)
