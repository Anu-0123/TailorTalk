
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from conversation import handle_conversation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    user_input = data.get("message")
    response = handle_conversation(user_input)
    return {"response": response}

