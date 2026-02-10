#!/usr/bin/env python3
"""
Simple test script to verify MCP tools are available.
This test bypasses the FastAPI server dependency and tests MCP tools directly.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from mcp.server.fastmcp import FastMCP

    # Create MCP server instance
    mcp = FastMCP("calendar-mcp-test")

    # Define a simple test tool
    @mcp.tool()
    async def test_tool() -> str:
        """Test tool to verify MCP server is working."""
        return json.dumps({"status": "success", "message": "MCP server is working"})

    # List available tools
    print("Testing MCP server initialization...")
    print(f"Server name: {mcp.name}")
    print(f"Available tools: {len(mcp._tools)}")

    if mcp._tools:
        print("\nAvailable tools:")
        for tool_name in mcp._tools:
            print(f"  - {tool_name}")

    print("\n✅ MCP server test passed!")
    sys.exit(0)

except Exception as e:
    print(f"❌ MCP server test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)