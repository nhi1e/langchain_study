from fastapi import FastAPI
from app.router import router

app = FastAPI(title="Tech Support Chatbot")
app.include_router(router) 