#pip install tiktoken
#pip install langchain

from langchain.chains.summarize import load_summarize_chain
from langchain import OpenAI
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

def summarize(text, api_key):
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(text)
    docs = [Document(page_content=t) for t in texts[:3]]
    
    os.environ["OPENAI_API_KEY"] = f"{api_key}"
    llm = OpenAI(temperature=0.75)
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)



