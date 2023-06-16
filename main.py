import os
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from dotenv import load_dotenv

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
