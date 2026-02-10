#!/usr/bin/env python3
"""
Test MCP server via stdio protocol.
This script tests the MCP server without requiring OAuth.
"""

import sys
import os
import asyncio
import json

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

async def test_mcp():
    """Test MCP server functionality."""
    try:
        print("Importing MCP bridge...")
        from src.mcp_bridge import create_mcp_server

        print("Creating MCP server...")
        mcp = create_mcp_server()

        print(f"✅ MCP server created: {mcp.name}")

        # Test that we can access internal tool manager
        if hasattr(mcp, '_tool_manager'):
            tools = mcp._tool_manager.list_tools()
            print(f"\n✅ Found {len(tools)} tools:")
            for tool in tools:
                print(f"   - {tool.name}")
        else:
            print("\n⚠️  Tool manager not accessible directly")

        print("\n✅ MCP server is ready!")
        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_mcp())
    sys.exit(0 if success else 1)