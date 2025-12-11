from fastapi import FastAPI
from pydantic import BaseModel
from g4f import ChatCompletion
from g4f.Provider import FreeGPT

app = FastAPI()

class CompletionRequest(BaseModel):
    model: str
    messages: list

@app.post("/v1/chat/completions")
async def chat(request: CompletionRequest):
    # Беремо повідомлення користувача
    messages = request.messages

    # Генеруємо відповідь тільки через FreeGPT
    result = ChatCompletion.create(
        model=request.model,
        provider=FreeGPT,  # фіксований провайдер
        messages=messages
    )

    # Повертаємо у форматі OpenAI
    return {
        "choices": [
            {
                "message": {
                    "content": result
                }
            }
        ]
    }
