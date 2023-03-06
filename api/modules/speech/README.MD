# Speech

This repository contains Python modules for working with speech data, including transcription and audio recording.

## Modules

### `transcribe.py`

This module provides a function for transcribing speech using OpenAI's GPT-3 language model. The `transcribe` function takes an audio file as input and returns a transcript of the speech as a string. The module requires the `openai` library to be installed.

### `record_audio.py`

This module provides a function for recording audio from the microphone and saving it as a .wav file. The `record_audio` function takes two optional arguments for the duration of the recording and the sample rate, and returns the filename of the saved audio file. The module requires the `sounddevice` and `scipy` libraries to be installed.

## Usage

To use the modules in your own Python projects, simply import them into your code:

```python
from speech.transcribe import transcribe
from speech.record_audio import record_audio
