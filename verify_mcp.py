#!/usr/bin/env python3
"""
Verify MCP bridge can be imported and server created.
"""

import sys
import os
import json

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    print("Importing mcp_bridge...")
    from src.mcp_bridge import create_mcp_server

    print("Creating MCP server...")
    mcp = create_mcp_server()

    print(f"✅ MCP server created successfully!")
    print(f"   Server name: {mcp.name}")
    print(f"   Server type: {type(mcp).__name__}")

    # Try to list tools
    try:
        tools = mcp.list_tools()
        print(f"\n✅ Found {len(tools)} tools:")
        for tool in tools:
            print(f"   - {tool.name}: {tool.description[:80]}...")
    except Exception as e:
        print(f"\n⚠️  Could not list tools: {e}")
        print("   (This may be expected, server creation was successful)")

    print("\n✅ MCP verification passed!")
    sys.exit(0)

except Exception as e:
    print(f"❌ MCP verification failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
