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

# ------------------------------------------------------------------------------------------------

from langchain_core.prompts import PromptTemplate
template = """
    You are a helpful assistant for classifying user queries in a tech support context.
    Your task is to determine the type of query based on the provided question.

    The possible query types are:
    - "sql": For queries related to customer account and support history.
    - "vectordb": For queries related to company policies, procedures, company-specific knowledge base
    - "web": For general web search queries or questions that do not fit the above categories

    Respond ONLY with one of the following values: sql, vectordb, web.
    Do not include explanations or natural language.

    Question: {question}
    Answer:
"""
custom_prompt = PromptTemplate.from_template(template)

# ------------------------------------------------------------------------------------------------
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

classifier_chain = (
    custom_prompt | llm | output_parser
)

def classify_query(question: str) -> str:
    response = classifier_chain.invoke({"question": question})
    return response

# Example usage:
if __name__ == "__main__":
    query = "how do i fix my broken laptop?"
    query_type = classify_query(query)
    print("Query:", query)
    print("Query type:", query_type)