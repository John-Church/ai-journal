from fastapi import FastAPI
import os

app = FastAPI()

JOURNAL_LOCATION = "./journal_entries"


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/followup/")
async def get_followup():
    return {"message":"followup"}

@app.get("/convo/")
async def get_all_conversations():
    for file in os.listdir('/journal_entries'):
        if file[-2:].lower() == "md":
            # File is a markdown file
            id, entry = file.split(".")[0].split("_")
    return {"message":"All the conversations"}

@app.get("/convo/{id}")
async def get_conversation(id):
    # Get the conversation of id from somewhere
    return {"message": f"Getting {id}"}

@app.post("/ingest/")
async def ingest_text(text: str):
    return text