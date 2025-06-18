import os
import getpass
from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

file_path = "./test.pdf"
loader = PyPDFLoader(file_path)
import asyncio

pages = []

async def load_pages():
    async for page in loader.alazy_load():
        pages.append(page)

asyncio.run(load_pages())
vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings())
docs = vector_store.similarity_search("What is the risks of cell-based food?", k=2)
for doc in docs:
    print(doc.page_content)
    print(doc.metadata)