from fastapi import FastAPI


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
    return {"message":"All the conversations"}

@app.get("/convo/{id}")
async def get_conversation(id):
    # Get the conversation of id from somewhere
    return {"message": f"Getting {id}"}

@app.post("/ingest/")
async def ingest_text(text: str):
    return text