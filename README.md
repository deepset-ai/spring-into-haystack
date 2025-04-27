<p align="center">
<img width="300" alt="Spring into haystack logo with flowers, bee and butterfly on the logo, giving spring vibes" src="/logo/spring-into-haystack-logo.png" />
</p>

Welcome to the 🌸 [Spring Into Haystack](https://haystack.deepset.ai/spring-into-haystack) 🌸 your chance to cultivate something useful, elegant, and powerful — just like spring itself! 🌼

## 🪻 Your Spring Challenge

Your mission is to build a **tool-using Haystack Agent** that acts as an **MCP Client** and connects to the [GitHub MCP Server](https://github.com/github/github-mcp-server). Once connected, your Agent will be able to call GitHub tools — all through the power of the Model Context Protocol.

To get started, check out the scaffolded starter code in [`github-agent.py`](src/github-agent.py). You’ll need to:
- Implement the missing parts
- Configure your Agent to connect to the GitHub MCP server
- Make sure the Agent can reason and act based on tool outputs

> Note: The [**official GitHub MCP Server**](https://github.com/github/github-mcp-server) requires **Docker** to run. If you're unable to use Docker (e.g. due to system limitations or permissions), you can use the [**legacy GitHub MCP Server**](https://github.com/modelcontextprotocol/servers/tree/main/src/github), which is **deprecated** but can be run easily run with `npx`. Note that the set of available tools differs between the official and legacy servers.

### ✅ Test Your Agent: Find the Hidden Typo

To verify your Agent is working correctly, we’ve planted a **typo somewhere in this very README**.

Once your Agent is fully wired up and reasoning correctly, it should:
1. **Detect the typo** by reading this README via the GitHub MCP server  
2. **Open a GitHub issue** describing the typo clearly in the issue body

This will prove that your Agent can:
- Understand the task and make a plan
- Select the right tool(s) from the GitHub MCP server
- Execute an action on GitHub

## 🌷 How to Participate

1. **Fork** this repo on GitHub
2. **Fill in the missing peices** in [`github-agent.py`](src/github-agent.py) to build your MCP-connected Agent
3. **Push your code** to your forked repo
4. **[Submit the link](https://forms.gle/VbyhQrKz1niyzBmGA) to the repo** so we can see your creation in full bloom!

For more info, check out [Spring Into Haystack](https://haystack.deepset.ai/spring-into-haystack) webpage.

## Start Building

### Requirements:

- A [GitHub Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with relevant permissions

### Install Dependencies

```
pip install -r requirements.txt
```
> Note: The `mcp-haystack` package requires Python ≥ 3.10

### Components:

- [`Agent`](https://docs.haystack.deepset.ai/docs/agent) – component for the smart decision-maker
- [`MCPTool`](https://docs.haystack.deepset.ai/docs/mcptool) – lets your agent talk to the MCP Server

### Environment Variables:

- `GITHUB_PERSONAL_ACCESS_TOKEN`: Your GitHub token
- `GITHUB_TOOLSETS`: Comma-separated list of GitHub toolsets to use
- `OPENAI_API_KEY`: Your OpenAI API key
- `GITHUB_OWNER`: Your GitHub username
- `GITHUB_REPO`: Your GitHub repository

### Running the Agent:
- Run from the root directory
```
python src/github-agent.py
```

> Note: The `mcp-haystack` package requires Python ≥ 3.10
