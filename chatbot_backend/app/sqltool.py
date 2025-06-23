

# need to get user id
# convert user query into SQL query
#--------------------------------------------------------------------------------------------------------
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
from langchain_community.utilities import SQLDatabase
import sqlite3
conn = sqlite3.connect("mock_support.db")
cursor = conn.cursor()
db = SQLDatabase.from_uri("sqlite:///mock_support.db", include_tables=["support_tickets"])
#--------------------------------------------------------------------------------------------------------
from typing_extensions import TypedDict

#schema for the final dictionary and pipeline
class State(TypedDict):
    user_id: str  # assuming user_id is provided in the input
    question: str
    query: str
    result: str
    answer: str

from langchain_core.prompts import ChatPromptTemplate
system_message = """
    You are a SQL expert tasked with generating syntactically correct and minimal SQL queries.

    The database contains user support ticket history. You are given a question from a user (in natural language), and you must output only a valid SQL query that retrieves the correct answer from the database.

    Follow these rules:
    - Only use the columns and tables listed in the schema below.
    - The main table is `support_tickets`. Relevant columns are:
            - user_id
            - issue
            - category
            - status
            - priority
            - created_at
            - updated_at
    - Always include a WHERE clause that uses the provided user_id (you will assume it's already known).
    - Order by `created_at` if looking for the most recent or latest ticket.
    - Use `LIMIT 1` if only one result is needed.
    - Return only the SQL query — no explanations, no natural language.

    Database Schema:
    {table_info}
"""

user_prompt = "User ID: {user_id}\nQuestion: {input}"

query_prompt_template = ChatPromptTemplate(
    [("system", system_message),
    ("human", user_prompt)],
)

# convert prompt to query using llm itself
from typing_extensions import Annotated

class QueryState(TypedDict):
    query: Annotated[str, ..., "A syntactically correct SQL query to run."] 

# populate parameters for the query prompt
def write_query(state: State):
    # Fill in the template with a dict, not kwargs
    prompt = query_prompt_template.invoke({
        "dialect": db.dialect,
        "top_k": 10,
        "table_info": db.get_table_info(),
        "input": state["question"],
        "user_id": state["user_id"]
    })

    structured_llm = llm.with_structured_output(QueryState)  # use the llm with structured output
    result = structured_llm.invoke(prompt)
    return result

#---------------------------------------------------------------------------------------------------------
# 2. execute the query: excexute the generated sql query
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool

def execute_query(state: State):
    execute_query_tool = QuerySQLDatabaseTool(db=db)            
    return {"result": execute_query_tool.invoke(state["query"])} # use the QuerySQLDataBaseTool to execute the query
#---------------------------------------------------------------------------------------------------------

# 3. generate answer from the result
def generate_answer(state: State):
    prompt = (
        "Given the following user question, corresponding SQL query, "
        "and SQL result, answer the user question.\n\n"
        f'Question: {state["question"]}\n'
        f'SQL Query: {state["query"]}\n'
        f'SQL Result: {state["result"]}'
    )
    response = llm.invoke(prompt)
    return {"answer": response.content}
#---------------------------------------------------------------------------------------------------------
from langgraph.graph import START, StateGraph
# build the pipeline using LangGraph
graph_builder = StateGraph(State).add_sequence(
    [write_query, execute_query, generate_answer]
)
# add entry point to tell graph where to start
graph_builder.add_edge(START, "write_query")
graph = graph_builder.compile()
#---------------------------------------------------------------------------------------------------------
for step in graph.stream({
    "question": "What was the issue with the most recent support ticket?",
    "user_id": "u005"
},stream_mode="updates" ):
    print(step)