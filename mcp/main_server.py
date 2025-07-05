from fastmcp import FastMCP
from latest_docs_server import latest_docs_mcp

main_mcp = FastMCP(
    name="Main MCP server"
)

main_mcp.mount("latest_docs_mcp", latest_docs_mcp)

if __name__ == "__main__":
    main_mcp.run(transport="sse", host="127.0.0.1", port=9000) 