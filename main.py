from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
import whisper
import shutil
import os
from datetime import datetime
from gtts import gTTS

app = FastAPI(title="BilingualBridge Sentiment Edition", version="2.9.0")

app.mount("/static", StaticFiles(directory="/opt/bilingual-bridge/static"), name="static")

LOG_DIR = "/opt/bilingual-bridge/verlauf"
os.makedirs(LOG_DIR, exist_ok=True)

print("Lade Whisper-Modell...")
whisper_model = whisper.load_model("base")
print("Whisper-Modell erfolgreich geladen!")

class PromptRequest(BaseModel):
    prompt: str
    model: str = "llama3"
    session_id: str = "default_session"
    slow_audio: bool = False
    agent_name: str = "Benno Engler"
    voice_tld: str = "com"

@app.get("/")
def read_root():
    return FileResponse("/opt/bilingual-bridge/static/index.html")

def log_to_server(session_id: str, sender: str, text: str):
    filename = f"{LOG_DIR}/session_{datetime.now().strftime('%Y-%m-%d')}.txt"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [Session: {session_id}] {sender}: {text}\n")

def is_english(text: str) -> bool:
    english_words = {"the", "is", "and", "to", "a", "of", "in", "for", "you", "that", "it", "he", "on", "with", "as", "be", "at", "have", "are", "this", "from", "by", "hot", "hello", "how", "can", "help", "my", "name", "number", "email", "address", "thank", "we", "your", "i", "not", "sure"}
    words = set(text.lower().split())
    intersection = words.intersection(english_words)
    return len(intersection) >= 2

def analyze_sentiment(text: str) -> str:
    """Lässt LLM kurz das Sentiment des Kunden bestimmen (neutral, warning, angry)"""
    try:
        prompt = f"Analyze the emotion of this customer support text and reply with EXACTLY ONE word: 'neutral', 'warning', or 'angry'. Text: '{text}'"
        res = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=3
        )
        ans = res.json().get("response", "").strip().lower()
        if "angry" in ans: return "angry"
        if "warning" in ans or "frustrated" in ans or "bad" in ans: return "warning"
        return "neutral"
    except:
        return "neutral"

@app.post("/api/generate")
def generate_response(req: PromptRequest):
    try:
        agent_label = req.agent_name.strip() or "Benno Engler"
        sentiment = "neutral"

        if is_english(req.prompt):
            # Wenn es englischer Text im Generator ist, behandeln wir es als Kundeneingabe und analysieren das Sentiment
            sentiment = analyze_sentiment(req.prompt)
            system_prompt = f"Translate the following English customer text naturally and fluently into German. Output ONLY the translated sentence without conversational filler. STRICT RULE FOR NUMBERS: Keep any numbers and digits 100% identical as digits. No quotes. Text: '{req.prompt}'"
            tts_lang = 'de'
            sender_name = "Kunde (EN - Text)"
            ai_name = f"{agent_label} / Übersetzung (DE)"
        else:
            system_prompt = f"Translate the following German support text naturally and fluently into English. Output ONLY the translated sentence without conversational filler. STRICT RULE FOR NUMBERS: Keep any numbers and digits 100% identical as digits. No quotes. Text to translate: '{req.prompt}'"
            tts_lang = 'en'
            sender_name = f"{agent_label} (DE - Text)"
            ai_name = "Kunde / Übersetzung (EN)"
        
        log_to_server(req.session_id, sender_name, req.prompt)

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={"model": req.model, "prompt": system_prompt, "stream": False}
        )
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Ollama Fehler: {response.text}")
        
        ai_response = response.json().get("response", "").strip().replace('"', '')
        log_to_server(req.session_id, ai_name, ai_response)

        audio_filename = f"/tmp/response_{os.getpid()}.mp3"
        tts = gTTS(text=ai_response, lang=tts_lang, slow=req.slow_audio, tld=req.voice_tld)
        tts.save(audio_filename)

        return {
            "response": ai_response,
            "audio_url": f"/api/audio/{os.path.basename(audio_filename)}",
            "sentiment": sentiment
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/bilingual-chat")
async def bilingual_chat(
    file: UploadFile = File(...), 
    session_id: str = Form("default_session"), 
    slow_audio: bool = Form(False),
    agent_name: str = Form("Benno Engler"),
    voice_tld: str = Form("com")
):
    try:
        agent_label = agent_name.strip() or "Benno Engler"
        temp_file_path = f"/tmp/{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        result = whisper_model.transcribe(temp_file_path, task="transcribe")
        user_text = result.get("text", "").strip()
        detected_lang = result.get("language", "de")

        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

        if not user_text:
            user_text = "Hello"

        sentiment = "neutral"

        if detected_lang == "en" or is_english(user_text):
            sentiment = analyze_sentiment(user_text)
            system_prompt = f"Translate the following English customer text naturally and fluently into German. Output ONLY the translated sentence without conversational filler. STRICT RULE FOR NUMBERS: Keep any numbers and digits 100% identical as digits. No quotes. Text: '{user_text}'"
            tts_lang = 'de'
            sender_name = "Kunde (Sprache EN)"
            ai_name = f"{agent_label} / Übersetzung (DE)"
        else:
            system_prompt = f"Translate the following German support text naturally and fluently into English. Output ONLY the translated sentence without conversational filler. STRICT RULE FOR NUMBERS: Keep any numbers and digits 100% identical as digits. No quotes. Text: '{user_text}'"
            tts_lang = 'en'
            sender_name = f"{agent_label} (Sprache DE)"
            ai_name = "Kunde / Übersetzung (EN)"
        
        log_to_server(session_id, sender_name, user_text)

        ollama_response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={"model": "llama3", "prompt": system_prompt, "stream": False}
        )
        ai_response = ollama_response.json().get("response", "").strip().replace('"', '')

        log_to_server(session_id, ai_name, ai_response)

        audio_filename = f"/tmp/bilingual_{os.getpid()}.mp3"
        tts = gTTS(text=ai_response, lang=tts_lang, slow=slow_audio, tld=voice_tld)
        tts.save(audio_filename)

        return {
            "user_transcript": user_text,
            "response": ai_response,
            "audio_url": f"/api/audio/{os.path.basename(audio_filename)}",
            "sentiment": sentiment
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/audio/{filename}")
def get_audio(filename: str):
    file_path = f"/tmp/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg")
    raise HTTPException(status_code=404, detail="Audiodatei nicht gefunden")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
