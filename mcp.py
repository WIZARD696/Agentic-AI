from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("My Agentic AI Server")


# Tool 1: Add two numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


# Tool 2: Multiply two numbers
@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b


# Tool 3: Get a greeting
@mcp.tool()
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello {name}! Welcome to Agentic AI."


# Tool 4: Get information about the project
@mcp.tool()
def project_info() -> str:
    """Return information about this MCP server."""
    return (
        "This is a beginner MCP server built with Python. "
        "It demonstrates how AI agents can use external tools."
    )


# Start the MCP server
if __name__ == "__main__":
    mcp.run()
