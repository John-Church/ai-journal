from fastapi import FastAPI, File
from modules.speech.transcribe import transcribe

from fastapi import FastAPI, File


app = FastAPI()

JOURNAL_LOCATION = "./journal_entries"


@app.post("/transcribe")
async def transcribe_endpoint(audio_file: bytes) -> str:
    """
    Transcribes an audio file using OpenAI's API.

    Args:
        audio_file (bytes, required): The audio file to be transcribed.

    Returns:
        str: The transcribed text.
    """
    transcript = transcribe(audio_file)
    return transcript
