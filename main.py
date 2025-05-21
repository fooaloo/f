from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Public API Example")

class Message(BaseModel):
    name: str
    message: str

@app.get("/ping")
def ping():
    return {"status": "online", "message": "API is live"}

@app.post("/say_hello")
def say_hello(msg: Message):
    return {"reply": f"Hello {msg.name}, you said: {msg.message}"}
