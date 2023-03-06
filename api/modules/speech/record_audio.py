import os
import sounddevice as sd
from scipy.io import wavfile as wf


def record_audio(duration: float = 5.0, sample_rate: int = 44100) -> str:
    """
    Records audio from the microphone for a specified duration and saves it as a .wav file.

    Args:
        duration (float): The duration of the recording in seconds. Defaults to 5.0 seconds.
        sample_rate (int): The sample rate of the recording in Hz. Defaults to 44100 Hz.

    Returns:
        str: The filename of the saved recording.
    """

    if not os.path.exists('audio'):
        os.makedirs('audio')

    print(f'Recording for {duration} seconds...')
    audio = sd.rec(int(sample_rate * duration),
                   samplerate=sample_rate, channels=1)

    sd.wait()

    filename = os.path.join('audio', 'recording.wav')
    wf.write(filename, int(sample_rate), audio)

    print(f'Recording saved as {filename}')

    return filename
