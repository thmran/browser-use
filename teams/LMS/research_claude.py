"""
Simple script that runs the task of opening amazon and searching.
@dev Ensure we have a `ANTHROPIC_API_KEY` variable in our `.env` file.
"""

import os
import sys
from dotenv import load_dotenv
from pydantic import SecretStr
from langchain_anthropic import ChatAnthropic

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('ANTHROPIC_API_KEY', '')

import asyncio

from browser_use import Agent

llm = ChatAnthropic(model_name='claude-3-5-sonnet-20241022', temperature=0.0, timeout=30, stop=None,api_key=SecretStr(api_key))

async def run_search():
    with open('../test_script/rtxprice.txt', 'r') as file:
        test_script = file.read()

    agent = Agent(
        task=test_script,
        llm=llm,
        use_vision=True,
        max_actions_per_step=10,
        save_conversation_path="logs/conversation.json"  # Save chat logs
    )

    result = await agent.run(max_steps=200)

if __name__ == '__main__':
    asyncio.run(run_search())