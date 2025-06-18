from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import getpass

# Load environment variables from .env file
load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

# schema (using pydantic)
class ResponseFormatter(BaseModel):
    """Structure the AI response with an answer and a follow-up question."""
    answer: str = Field(description="The answer to the user's question")
    followup_question: str = Field(description="A followup question the user could ask")

class DefinitionSchema(BaseModel):
    """Define the schema for the response."""
    term: str = Field(description="The term being defined")
    definition: str = Field(description="The definition of the term")
    example: str = Field(description="An example of the term in use")

#Load the model
model = ChatOpenAI(model="gpt-4", temperature=0) #temperature is the randomness of the model's output

#follow up question
# Bind schema to the model (using with_structured_output)
#model_structured = model.with_structured_output(ResponseFormatter)
#infer
#structured_output = model_structured.invoke("What is the powerhouse of the cell?")

#definition
# model_structured = model.with_structured_output(DefinitionSchema)
# structured_output = model_structured.invoke("What is a mitochondria?")

#tool calling
model_with_tools = model.bind_tools([DefinitionSchema])
ai_response = model_with_tools.invoke("What is the definition of human?")

print(ai_response.content)