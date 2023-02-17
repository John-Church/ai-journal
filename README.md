# ai-journal
Welcome to the AI journal project!! Our goal is to create an open source AI assistant to help record your daily journal. this project is still in plannign stages.

## MVP
A user should be able to open the app and narrate a journal entry. The assistant will then ask followup questions to prompt the user to narrate a more complete entry. That narration, after being converted from speech to text, will be formatted by an LLM into a journal entry. Those entries will be embedded for an easy search experience and possible chat interface.

The MVP will include:
- A voice to text UI interface to record your thoughts
- An assistant that asks followup questions to prompt you to add more to your journal
- An LLM chain built with LangChain to format your journal
- An embedding enabled search interface

Possible next features include:
- A chat bot to ask questions about your own journal

We are currently in planning stages so this is all subject to change. System architecture is still in planning stages. Main concerns are ease of deployment for non-technical users and maintainability. Options include:
- a standalone downloadable electron desktop app
- a full backend and frontend deployed solution with plans to host it as a service for non technical users (eg open source the code but provide a paid service already hosted- profits go to server maintenance and then a 501c3)
