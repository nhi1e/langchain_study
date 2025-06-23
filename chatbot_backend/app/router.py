from fastapi import APIRouter
from app.models import ChatRequest, ChatResponse
from app.classifier import classify_query
from app.tavily_tool import search_web
from app.sql_tool import query_support_ticket
from app.vectordb_tool import retrieve_doc

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    query_type = classify_query(request.query)

    #need to restructure the parameter to match the function signature
    if query_type == "sql":
        response = query_support_ticket(request.user_id)
    elif query_type == "vectordb":
        response = retrieve_doc(request.message)
    elif query_type == "web":
        response = await search_web(request.message)
    else:
        response = "Error"

    return ChatResponse(query_type=query_type, response=response)