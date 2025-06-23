import getpass
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

os.environ["LANGCHAIN_TRACING_V2"] = "true"

load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
if "LANGCHAIN_API_KEY" not in os.environ:
    os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("Enter your LangChain API key: ")

llm = ChatOpenAI(model="gpt-4o-mini")

#--------------------------------------------------------------------------------------------------------
from langchain_community.document_loaders import PyPDFLoader
#load
file_path = os.path.join(os.path.dirname(__file__), "mock_data", "Mock_Company_Policies.pdf")
loader = PyPDFLoader(file_path) # extracts text from PDF file
docs = loader.load()  # create langchain document for each page of the pdf (page content + metadata)
#--------------------------------------------------------------------------------------------------------
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma             # vector store
from langchain_openai import OpenAIEmbeddings   # embedding model
# split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200, 
)
all_splits = text_splitter.split_documents(docs)
#embed
vector_store = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())
#retrieve
retriever = vector_store.as_retriever()
#--------------------------------------------------------------------------------------------------------
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

system_prompt = (
    """
        You are a helpful assistant for answering questions based on the content of a PDF document.
        Use the following pieces of context to answer the question.
        If you don't know the answer, just say that you don't know, don't try to make
        up an answer. Use maximum 3 sentences to keep the answer concise.

        Context: {context}
    """
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
qa_chain = create_stuff_documents_chain(llm, prompt)    # 2. inject context into the prompt and pass to LLM
rag_chain = create_retrieval_chain(retriever, qa_chain) # 1. retrieve data, passes to qa_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

system_prompt = (
    """
        You are a helpful assistant for answering questions based on the content of a PDF document.
        Use the following pieces of context to answer the question.
        If you don't know the answer, just say that you don't know, don't try to make
        up an answer. Use maximum 3 sentences to keep the answer concise.

        Context: {context}
    """
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"), #create_retrieval_chain expects "input" keyword
    ]
)
qa_chain = create_stuff_documents_chain(llm, prompt)    # 2. inject context into the prompt and pass to LLM
rag_chain = create_retrieval_chain(retriever, qa_chain) # 1. retrieve data, passes to qa_chain

# results = rag_chain.invoke({"input": "How do I request a day off?"})
# print(results["answer"] if "answer" in results else "No relevant documents found.")
#--------------------------------------------------------------------------------------------------------
async def retrieve_doc(query: str):
    """
    Function to retrieve relevant documents from the vector store based on the query.
    """
    results = rag_chain.invoke({"input": query})
    return results["answer"] if "answer" in results else "No relevant documents found."
