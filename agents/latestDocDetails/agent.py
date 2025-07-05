from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import(
    MCPToolset,
    SseConnectionParams
)
from . import prompt
import os
from dotenv import load_dotenv

load_dotenv()

latest_doc_details_agent=LlmAgent(
    name="lastest_docs",
    description="An agent that retrieves the latest document details from connected libraries.",
    model="gemini-1.5-flash-latest",
    instruction=prompt.LATEST_DOC_PROMPT,
    tools=[
        MCPToolset(
            connection_params=SseConnectionParams(url="http://localhost:9000/sse")
        )
    ],
    output_key="latest_doc_details_agent_output"
)