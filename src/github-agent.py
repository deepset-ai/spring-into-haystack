import os
from pathlib import Path

from dotenv import load_dotenv
from haystack.components.agents import Agent
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack_integrations.tools.mcp import MCPToolset, StdioServerInfo

# 1. Load secrets --------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
load_dotenv(ENV_PATH)

token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
if not token:
    raise RuntimeError("Add GITHUB_PERSONAL_ACCESS_TOKEN to .env")

toolsets = os.getenv("GITHUB_TOOLSETS")
if not toolsets:
    raise RuntimeError("Add GITHUB_TOOLSETS to .env")

# 2. StdioServerInfo -----------------------------------------------------------
docker_args = ["run", "-i", "--rm"]
if ENV_PATH.exists():
    docker_args += ["--env-file", str(ENV_PATH)]
docker_args += ["ghcr.io/github/github-mcp-server:latest"]
docker_env = {"GITHUB_PERSONAL_ACCESS_TOKEN": token}
if toolsets:
    docker_env["GITHUB_TOOLSETS"] = toolsets
github_mcp_server = StdioServerInfo(
    command="docker",
    args=docker_args,
    env=docker_env,
)
print("✅ MCP server definition created")

# 3. Grab all GitHub tools -----------------------------------------------------
github_tools = MCPToolset(server_info=github_mcp_server)

# 4. Build the Agent -----------------------------------------------------------
agent = Agent(
    chat_generator=OpenAIChatGenerator(model="gpt-4o-mini", tools=github_tools),
    tools=github_tools,
    system_prompt=(
        "You are an engineering assistant who can read and modify GitHub "
        "repositories via the MCP tools I’ve given you. "
        "Whenever useful, call tools rather than answering from memory."
    ),
)
print("✅ Agent created")

# 5. Test-drive ---------------------------------------------------------------
print("\n=== Test-drive ===")
github_owner = os.getenv("GITHUB_OWNER")
github_repo = os.getenv("GITHUB_REPO")
if not github_owner or not github_repo:
    raise RuntimeError("Add GITHUB_OWNER and GITHUB_REPO to .env")
print(f"Using {github_owner}/{github_repo}")
user_input = (
    f"Can you find the typo in the README of {github_owner}/{github_repo}.git "
    "and open an issue describing how to fix it?"
)
response = agent.run(messages=[ChatMessage.from_user(text=user_input)])

print("\n=== Full agent trace ===")
for m in response["messages"]:
    print(f"{m.role.upper():7}: {m.text}")

print("\n=== Final answer ===")
print(response["messages"][-1].text)
