from tavily import TavilyClient
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
if "TAVILY_API_KEY" not in os.environ:
    raise ValueError("TAVILY_API_KEY is not set in the environment variables.")

client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

async def search_web_with_tavily(query: str) -> str:
    result = client.search(query=query, max_results=3)
    return result["results"][0]["content"] if result["results"] else "No info found."

#---------------------------------------------------------------------------------------------------
import getpass
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   

os.environ["LANGCHAIN_TRACING_V2"] = "true"

load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
if "LANGCHAIN_API_KEY" not in os.environ:
    os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("Enter your LangChain API key: ")

llm = ChatOpenAI(model="gpt-4o-mini")

template = """
    You are a helpful assistant for question-answering tasks.
    Use the following pieces of context to answer the question at the end, clearly and concisely.

    Context: {context}
    Question: {question}
    Helpful Answer:
"""
custom_prompt = PromptTemplate.from_template(template)

output_parser = StrOutputParser()

rag_chain = custom_prompt | llm | output_parser 
#---------------------------------------------------------------------------------------------------
# if __name__ == "__main__":
#     query = "How do i fix my broken laptop?"
#     context = asyncio.run(search_web_with_tavily(query))
#     response = rag_chain.invoke({"context": context, "question": query})
#     print("Query:", query)
#     print("Response:", response)
#---------------------------------------------------------------------------------------------------
async def search_web(query: str) -> str:
    context = await search_web_with_tavily(query)
    response = rag_chain.invoke({"context": context, "question": query})
    return response
