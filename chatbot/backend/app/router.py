from fastapi import APIRouter
from app.models import ChatRequest, ChatResponse
from app.classifier import classify_query
from app.tavily_tool import search_web
from app.sql_tool import query_support_ticket
from app.vectordb_tool import retrieve_doc

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    print("Received request:", request)
    query_type = classify_query(request.message)
    print("Classified query as:", query_type)

    try:
        if query_type == "sql":
            response = await query_support_ticket(request.user_id, request.message)
        elif query_type == "vectordb":
            response = await retrieve_doc(request.message)
        elif query_type == "web":
            response = await search_web(request.message)
        else:
            response = "Sorry, I can only answer questions related to tech support."

        print("Response to send:", response)
        return ChatResponse(query_type=query_type, response=response)
    except Exception as e:
        print("Error during processing:", e)
        return ChatResponse(query_type="error", response="Backend error occurred.")
