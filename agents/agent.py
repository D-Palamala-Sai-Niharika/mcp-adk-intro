import os
from google.adk.agents import LlmAgent 
from dotenv import load_dotenv
from . import prompt
from agents.latestDocDetails.agent import latest_doc_details_agent

# Full path to the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

root_agent=LlmAgent(
    name="modern_assistant",
    description="You are a modern assistant agent that helps in providing travel assistance with details to the user, real-time weather details and updated documentation code",
    model="gemini-1.5-flash-latest",
    instruction=prompt.MAIN_AGENT_PROMPT,
    sub_agents=[latest_doc_details_agent]
    # tools="",
    # output_key=""
)