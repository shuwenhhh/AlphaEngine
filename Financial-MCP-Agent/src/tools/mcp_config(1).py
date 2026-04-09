"""
MCP服务器配置模块 - 包含连接A股MCP服务器的配置信息
"""

SERVER_CONFIGS = {
    "a_share_mcp_v2": {  
        "command": "uv", 
        "args": [
            "run",  
            "--directory",
            r"/root/code/Finance/a-share-mcp-is-just-i-need",  # 修改为a-share-mcp-is-just-i-need服务器项目路径
            "python",  #
            "mcp_server.py"  # MCP服务器脚本
        ],
        "transport": "stdio",
    }
}