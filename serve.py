### Open AI API Key and Open Source models--Llama3,Gemma2,mistral--Groq
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")

model=ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)

# Create Prompt template
context= "Translate the following into {language}"
prompt= ChatPromptTemplate.from_messages(
    [("system", context),("user", "{text}")]
)

parser= StrOutputParser()

##create chain
chain=prompt|model|parser

# App definition
app= FastAPI(title="Langchain Server", version="1.0", description= "A simple API server using Langchain runnable interfaces")

## Adding chain routes
add_routes(app, chain, path="/chain")

import uvicorn
if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
    






