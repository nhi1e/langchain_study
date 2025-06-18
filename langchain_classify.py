import os
import getpass
from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
    
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model

llm = init_chat_model("gpt-4o-mini", model_provider="openai")

#from_template allows you to create a prompt template from a string.
tagging_prompt = ChatPromptTemplate.from_template(
    """ 
        You are a helpful assistant in extracting specific properties from a passage.
        Extract the desired information from the following passage.

        Only extract the properties mentioned in the 'Classification' function.

        Passage: {passage}
    """
)

class Classification(BaseModel):
    sentiment: str = Field(description="The sentiment of the passage")
    agression: str = Field(description="The aggression level of the passage from 0 to 10")
    language: str = Field(description="The language of the passage")

structured_llm = llm.with_structured_output(Classification)

psg = "Tao ghét mày"
prompt = tagging_prompt.invoke({"passage":psg}) #{passage} placeholder in the template is replaced with psg
response = structured_llm.invoke(prompt)
print(response)
