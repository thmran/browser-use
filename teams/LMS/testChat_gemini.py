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

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

async def run_search():
    with open('../test_script/test_script.txt', 'r') as file:
        test_script = file.read()

    agent = Agent(
        task=test_script,
        llm=llm,
        use_vision=True,
        max_actions_per_step=10,
    )

    await agent.run(max_steps=200)

if __name__ == '__main__':
    asyncio.run(run_search())