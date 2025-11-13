import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.chat import user_chat

load_dotenv()

app =  FastAPI(title="Alixia AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins = [f'{os.getenv('CORS_ALLOWED_ORIGINS')}'],
    allow_credentials= False,
    allow_methods = ['POST'],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Welcome to Alixia AI"


class chatAlixiaAIRequest(BaseModel):
    message: str 

@app.post('/chat')
async def chatWithAlixiaAi(req: chatAlixiaAIRequest):
    text = req.message
    if not text:
        return JSONResponse(content={"error": 'No text provided' }, status_code=400)
    try:
        print('Message: ', req.message)
        genai_response = user_chat(text)
        return JSONResponse(content={'response': genai_response}, status_code=200)
    except Exception as e:
        print(str(e))
        return JSONResponse(content={'response': str(e)}, status_code=500)