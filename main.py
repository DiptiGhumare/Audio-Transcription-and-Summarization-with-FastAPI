from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
import shutil
from datetime import datetime

from transcription import transcribe_audio
from summarization import summarize_text
from data import save_transcription, save_summary, save_timestamps

app = FastAPI()

# CORS settings
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SAVE_DIR = "results"
os.makedirs(SAVE_DIR, exist_ok=True)

class TranscriptionResponse(BaseModel):
    transcription: str
    summary: str
    timestamps: list

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio_endpoint(file: UploadFile = File(...)):
    try:
        # Ensure the uploads directory exists
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        # Save the uploaded file
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Perform transcription
        transcription, timestamps = transcribe_audio(file_path)

        # Perform summarization
        summary = summarize_text(transcription)

        # Save results locally
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_transcription(transcription, SAVE_DIR, file.filename, timestamp)
        save_summary(summary, SAVE_DIR, file.filename, timestamp)
        save_timestamps(timestamps, SAVE_DIR, file.filename, timestamp)

        # Return response with transcription, summary, and timestamps
        return TranscriptionResponse(
            transcription=transcription,
            summary=summary,
            timestamps=timestamps
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
