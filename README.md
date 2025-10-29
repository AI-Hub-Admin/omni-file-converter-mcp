# omni-file-converter-mcp

[![MCP Marketplace User Review Rating Badge](https://www.deepnlp.org/api/marketplace/svg?name=AI-Hub-Admin/omni-file-converter-mcp)](https://www.deepnlp.org/store/mcp-server/mcp-server/pub-AI-Hub-Admin/omni-file-converter-mcp) |
[![AI Agent Marketplace DeepNLP](https://www.deepnlp.org/api/ai_agent_marketplace/svg?name=AI-Hub-Admin/bing-image-search-mcp)](https://www.deepnlp.org/store/mcp-server/mcp-server/pub-AI-Hub-Admin/bing-image-search-mcp) |[GitHub](https://github.com/AI-Hub-Admin/omni-file-converter-mcp)

Omni File Format converter MCP With No Access Key Requested.

This MCP server aims to convert various formats of documents to your desired formats.


## Tool

### 1. pdf_to_image

Args: 

file_path: Str, Local Folder Path of your Input PDF File 
output_format: Str, 
output_file_name: The output image file name, if not specified, use the same name as input file path file_name.pdf will output file_name_1.jpg, file_name_2.jpg, etc. 

Return: 

str: json str with below values samples [ {'output_path': '/your_local_folder/output_name_1.jpg'}, {'output_path': '/your_local_folder/output_name_2.jpg'}, {'output_path': '/your_local_folder/output_name_3.jpg'}, ]



### Usage 

### Try on the playground of MCP Tool Use Agent Web

[MCP Tool Use Agent Web](https://agent.deepnlp.org) 

Find Agent Information on Agent Meta on [Marketplace](https://agent.deepnlp.org/store/ai-agent/mcp-server/AI-Hub-Admin/omni-file-converter-mcp)

[Omni File Convert MCP Playground](https://agent.deepnlp.org/agent/mcp_tool_use?server=AI-Hub-Admin/omni-file-converter-mcp)

[Example Share URL of PDF to Image File Format Convert](https://agent.deepnlp.org/agent/mcp_tool_use/share/9f390a91-81f1-46ad-bcc0-3ed176d3f42e)


**Tool Calling Results**



### Client Usage (Cursor,VS Code and more)

#### 1. OneKey MCP Router Http Server Config

StreamingHttpConnection 

Supporting ONEKEY Router Access Beta Test Keys 
```
DEEPNLP_ONEKEY_ROUTER_ACCESS=BETA_TEST_KEY_OCT_2025
```
You can also generate your personal unlimited rate keys here [OneKey](https://www.deepnlp.org/workspace/keys) and Seee the onekey mcp router Demo [Google Maps MCP Server OneKey Example](https://www.deepnlp.org/store/mcp-server/map/pub-google-maps/google-maps) for reference on how to use one access key to access commercial MCPs.

```
{
    "mcpServers": {
		"omni-file-converter-mcp": {
			"url": "https://agent.deepnlp.org/mcp?server_name=omni-file-converter-mcp&onekey=BETA_TEST_KEY_OCT_2025"
		}
    }
}
```


### 2. Running Locally


##### Install
```
uv pip install pymupdf
```

##### MCP Integration


##### GitHub Source Running Localing
```
git clone https://github.com/AI-Hub-Admin/omni-file-converter-mcp
cd omni-file-converter-mcp

```

Run From Your Local Folder

```
{
    "mcpServers": {
        "omni-file-converter-mcp": {
            "command": "uv",
            "args": ["--directory", "/path_to_folder/omni-file-converter-mcp/src/omni_file_converter_mcp", "run", "server.py"]
        }
    }
}
```


#### AI Agent Marketplace Index And Router Support
[![AI Agent Marketplace And Router](https://www.deepnlp.org/api/ai_agent_marketplace/svg?name=AI-Hub-Admin/omni-file-converter-mcp)](https://deepnlp.org/store/ai-agent/ai-agent-marketplace/pub-AI-Hub-Admin/omni-file-converter-mcp)
```
curl 'https://www.deepnlp.org/api/ai_agent_marketplace/v2?id=AI-Hub-Admin/omni-file-converter-mcp'
```
    