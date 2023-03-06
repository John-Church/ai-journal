from fastapi import FastAPI


app = FastAPI()

JOURNAL_LOCATION = "./journal_entries"


@app.get("/")
async def root():
    return {"message": "Hello World"}
