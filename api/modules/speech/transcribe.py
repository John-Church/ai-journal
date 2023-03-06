import openai


def transcribe(audio_path: str) -> str:
    """
    Transcribes an audio file using OpenAI's API.

    Args:
        audio_file_path (str): The path to the audio file to be transcribed.

    Returns:
        str: The transcribed text.
    """
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript


transcribe("recording.wav")
