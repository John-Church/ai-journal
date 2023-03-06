import openai
from fastapi import File


def transcribe(audio_file: bytes) -> str:
    """
    Transcribes an audio file using OpenAI's API.

    Args:
        audio_file (bytes): The audio file to be transcribed.

    Returns:
        str: The transcribed text.
    """
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
    return transcript
