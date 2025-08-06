from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from gtts import gTTS
import uuid
import os

app = FastAPI()

class TTSRequest(BaseModel):
    text: str
    lang: str = "ko"

@app.post("/tts")
async def tts(request: TTSRequest):
    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(text=request.text, lang=request.lang)
    tts.save(filename)
    return FileResponse(filename, media_type="audio/mpeg", filename="speech.mp3")

@app.get("/")
def root():
    return {"message": "TTS 서버가 실행 중입니다."}