## Endpoints
/post Endpoint to send an audio transcription
returns text of the transcription 

/Get endpoint receive follow up questions



/get endpoint add summaries of all conversations and ids

/get endpoint to get a single conversation by its id. 


/Post ingest raw text of the converstation (json)

```json
[
    {"content": "Bla bla bla",
    "source": "User"
    },
    {
        "content": "Ayy, LMAO",
        "source": "Server",
    }
]
```