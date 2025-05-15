from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.components.agents import Agent
from haystack_integrations.tools.mcp import MCPTool, StdioServerInfo, MCPToolset

## Legacy GitHub MCP Server
github_mcp_server = StdioServerInfo(
    command="npx", 
    args=["-y", "@modelcontextprotocol/server-github"], 
    env={
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR GITHUB TOKEN>"
      })

## Official GitHub MCP Server
github_mcp_server = StdioServerInfo(
    command="docker", 
    args=[
          "run",
          "-i",
          "--rm",
          "-e",
          "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ], 
    env={
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR GITHUB TOKEN>"
      })

print("MCP server is created")

## Add tools manually
create_issue = MCPTool(
    name="create_issue",
    server_info=github_mcp_server,
    description="Use this tool to create issues on the given github repository"
)

get_file_contents = MCPTool(
    name="get_file_contents",
    server_info=github_mcp_server
)

tools = [create_issue, get_file_contents]

## Alternatively, load available tools automatically with MCPToolset
## You can load all tools in this server if you don't specify `tool_names`

# tools = MCPToolset(server_info=github_mcp_server, tool_names=["create_issue", "get_file_contents"]) 

print("MCP tools are created")

agent = Agent(
    chat_generator=OpenAIChatGenerator(model="gpt-4o-mini"),
    tools=tools,
    system_prompt="""
    You are a helpful agent that uses the tools that are provided. 
    Split the task into smaller tasks if necessary. Don't ask for confirmation
    """
)

print("Agent created")

## Example query to test your agent
user_input = "Can you find the typo in the README of <owner/repo> and open an issue about how to fix it?"

response = agent.run(messages=[ChatMessage.from_user(text=user_input)])

## Print the agent thinking process
print(response)
## Print the final response
print(response["messages"][-1].text)