from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    query_type: str
    response: str = Field("", description="The response message from the chatbot")