import os

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.indexes import VectorstoreIndexCreator
import gradio as gr
import time

from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter


from langchain.document_loaders import (
    Docx2txtLoader,
    UnstructuredPDFLoader,
    PyPDFLoader,
    PyMuPDFLoader,
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
        #loader = UnstructuredPDFLoader(document_path)
        loader = PyMuPDFLoader(document_path)
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

print("source_documents", source_documents)

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
chunked_docs = splitter.split_documents(source_documents)
#Use OPEN AI embeddings
embedder = OpenAIEmbeddings()

#create a vector Store
vector_store = FAISS.from_documents(chunked_docs, embedder)

print("vector_store:", vector_store)


chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=vector_store.as_retriever(), input_key="question")

with gr.Blocks() as chatagent:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")
    history = []

    def user(query, history):
        print("user_message", query)
        print("Chat History:", history)
        # Get response from  chain
        response = chain.run(query)
        # Append user message and response to chat history
        history.append((query, response))
        time.sleep(1)
        return "", history

    msg.submit(user, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

chatagent.launch(debug=True)
    
