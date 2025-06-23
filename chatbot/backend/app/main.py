from fastapi import FastAPI
from app.router import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Tech Support Chatbot")
app.include_router(router) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # allow your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
