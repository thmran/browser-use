import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import Agent

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-pro-exp-02-05', api_key=SecretStr(api_key))

async def run_search():
    with open('../test_script/createBookLO_script.txt', 'r') as file:
        test_script = file.read()

    agent = Agent(
        task="search price of ipad on amazon and get best price",
        llm=llm,
        use_vision=True,
        max_actions_per_step=10,
        save_conversation_path="logs/conversation.json"  # Save chat logs
    )

    result = await agent.run(max_steps=200)

if __name__ == '__main__':
    asyncio.run(run_search())