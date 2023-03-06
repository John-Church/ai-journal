import modal
from main.py import app

stub = modal.Stub()

image = (
    modal.Image.debian_slim()
    # .pip_install("langchain")
    # .pip_install("openai")
    # .pip_install("python-dotenv")
    # .pip_install("openai-whisper")
)


@stub.asgi(image=image)
def fastapi_app():
    return app
