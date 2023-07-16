# Import necessary libraries
import os
import sys

# Import OpenAI and LangChain libraries
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

# Import constants
import constants

# Set OpenAI API Key from constants
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

# Check if the script received any argument, if so, set it as the initial query
query = None
if len(sys.argv) > 1:
  query = sys.argv[1]

# If PERSIST flag is true and a persisted index exists, load vectorstore from the persisted data
# Create index from the vectorstore
# Otherwise, load documents from the data directory
# If PERSIST flag is true, create a persisted index from the loaded documents
# Else, create a non-persisted index from the loaded documents
if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  #loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
  loader = DirectoryLoader("datastore/")
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

# Initialize the conversational retrieval chain with the GPT-3 model and the created index
chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

# Initialize chat history
chat_history = []

# Start the conversation loop
while True:
  # If no query is currently set, prompt the user for a new query
  if not query:
    query = input("Prompt: ")
  
  # If the query is a quit command, terminate the program
  if query in ['quit', 'q', 'exit']:
    sys.exit()
  
  # Use the conversational retrieval chain to generate a response
  result = chain({"question": query, "chat_history": chat_history})
  
  # Display the answer
  print(result['answer'])

  # Add the query and answer to the chat history
  chat_history.append((query, result['answer']))
  
  # Clear the current query
  query = None
