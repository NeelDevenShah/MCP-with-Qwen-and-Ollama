from mcp.server.fastmcp import FastMCP
import subprocess
import requests
import logging
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

mcp = FastMCP(
    name="Qwen3 Enterprise MCP",
    description="Robust MCP server for enterprise AI with Qwen3",
    dependencies=["requests"]
)

@mcp.tool()
def execute_python_code(code: str) -> str:
    """Execute Python code and return the output."""
    try:
        result = subprocess.run(
            ["python", "-c", code],
            capture_output=True,
            text=True,
            timeout=15
        )
        output = result.stdout or result.stderr
        return output
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def fetch_web_content(url: str, max_length: int = 5000) -> str:
    """Fetch content from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.text[:max_length]
        return content
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.prompt()
def analyze_web_content(url: str) -> str:
    """Analyze web content using Qwen3."""
    return f"""You are an expert analyst. Use the fetch_web_content tool to retrieve content from {url}, then use the generate_text tool to summarize the content in 100 words or less. Provide key insights and conclusions."""

if __name__ == "__main__":
    mcp.run()
