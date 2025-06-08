import asyncio
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    # Create configuration dictionary
    config = {
  "mcpServers": {
    "custom_server": {
      "command": "python",
      "args": ["server2.py"],  # Relative path if running from same directory
      "cwd": "/home/neelshah",  # Set working directory
      "env": {}
    }
  }
}

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatOllama(model="qwen3:4b", temperature=0.7)

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Get me details from the kimaxpolytron.com",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
