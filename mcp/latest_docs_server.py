from fastmcp import FastMCP
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import json
import os
import httpx

# Full path to the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

latest_docs_mcp = FastMCP(
    name="latest Documentation"
)

USER_AGENT = "docs-app/1.0"
SERPER_API_URL = "https://google.serper.dev/search"

doc_urls={
    "langchain" : "python.langchain.com/docs",
    "llama-index" : "docs.llamaindex.ai/en/stable",
    "openai" : "platform.openai.com/docs"
}

async def search_web(query:str) -> dict | None :
    """
    Serper api playground - 
    serper api call to fetch latest documentation or top 2 latest links on google
    """

    payload = json.dumps({"q": query,"num": 2})

    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SERPER_API_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            print(response.text)
            return response.json()
        except httpx.TimeoutException:
            return "Time out Error - Search Web"

async def fetch_docs_from_url(url:str):
    async with httpx.AsyncClient() as client:
        try:
            response=await client.get(url,timeout=30.0)
            soup=BeautifulSoup(response.text,"html.parser")
            text=soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Time out Error - Fetch Docs from url"
        
    

@latest_docs_mcp.tool()
async def get_docs(query:str,library:str):
     """
     Search the latest docs for a given query and library.
     Tool Supports langchain, openai, and llama-index only for now
     
     Args: 
     query: The query to search for (e.g. "Chroma DB")
     library: The library to search in (e.g. "langchain")
     
     Returns:
     Text from latest documentation

     User Input Example :
     Provide me documentation on ChromaDB from langchain
     """

     if library not in doc_urls:
         raise ValueError(f"Libary {library} is not supported by the tool")
     
     final_query=f"site:{doc_urls[library]} {query}"
     results = await search_web(final_query)
     if len(results["organic"])==0:
         return "No Resouces Found"
     
     text=""
     for result in results["organic"]:
         text+=await fetch_docs_from_url(result["link"])
         return text
     
     
