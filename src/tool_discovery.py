import json
from pathlib import Path


class MCPServerConfig:
    """
    Loads MCP server configuration from servers.json.
    """

    def __init__(self, config_path: str = "servers.json"):
        self.config_path = Path(config_path)

    def load(self) -> dict:
        with self.config_path.open("r", encoding="utf-8") as file:
            return json.load(file)