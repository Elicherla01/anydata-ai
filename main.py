import os

from langchain.indexes import VectorstoreIndexCreator

from langchain.document_loaders import (
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    EverNoteLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)


from dotenv import load_dotenv

import os

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

print("OPENAI_API_KEY", OPENAI_API_KEY)

        
source_documents = []
count = -1
for file in os.listdir("source_data"):
    count += 1
    if file.endswith(".pdf"):
        document_path = "./source_data/" + file
        loader = PyPDFLoader(document_path)
        source_documents.extend(loader.load())
        
    elif file.endswith('.docx') or file.endswith('.doc'):
        document_path = "./source_data/" + file
        loader = Docx2txtLoader(document_path)
        source_documents.extend(loader.load())
        
    elif file.endswith('.txt'):
        document_path = "./source_data/" + file
        loader = TextLoader(document_path)
        source_documents.extend(loader.load())
    
    elif file.endswith('.csv'):
        document_path = "./source_data/" + file
        loader = CSVLoader(document_path)
        source_documents.extend(loader.load())
        
    elif file.endswith('.doc'):
        document_path = "./source_data/" + file
        loader = UnstructuredWordDocumentLoader(document_path)
        source_documents.extend(loader.load())
    
    elif file.endswith('.epub'):
        document_path = "./source_data/" + file
        loader = UnstructuredEPubLoader(document_path)
        source_documents.extend(loader.load())
    
    elif file.endswith('.html'):
        document_path = "./source_data/" + file
        loader = UnstructuredHTMLLoader(document_path)
        source_documents.extend(loader.load())
        
    elif file.endswith('.md'):
        document_path = "./source_data/" + file
        loader = UnstructuredMarkdownLoader(document_path)
        source_documents.extend(loader.load())
        
    elif file.endswith('.odt'):
        document_path = "./source_data/" + file
        loader = UnstructuredODTLoader(document_path)
        source_documents.extend(loader.load())
        
    elif file.endswith('.ppt'):
        document_path = "./source_data/" + file
        loader = UnstructuredPowerPointLoader(document_path)
        source_documents.extend(loader.load())
        
    elif file.endswith('.enex'):
        document_path = "./source_data/" + file
        loader = EverNoteLoader(document_path)
        source_documents.extend(loader.load())
    
    elif file.endswith('.eml'):
        document_path = "./source_data/" + file
        loader = UnstructuredEmailLoader(document_path)
        source_documents.extend(loader.load())

        
print("I processed",count , "documents")   

