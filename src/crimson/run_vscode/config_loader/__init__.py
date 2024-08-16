import os
import yaml
import json
from typing import Optional, Any


class ConfigLoader:
    def __init__(self, config_filename: str = ".run_vscode", default_config: Optional[dict] = None):
        self.config_filename = config_filename
        self.default_config = default_config or {}
        self.config = self.load_config()

    def find_config_file(self) -> Optional[str]:
        current_dir = os.getcwd()
        while current_dir != os.path.dirname(current_dir):
            potential_path = os.path.join(current_dir, self.config_filename)
            if os.path.exists(potential_path):
                return potential_path
            current_dir = os.path.dirname(current_dir)
        return None

    def load_config(self) -> dict:
        config_file_path = self.find_config_file()
        if config_file_path:
            with open(config_file_path, "r") as f:
                config = yaml.safe_load(f) or {}
        else:
            config = {}

        # Merge with default_config
        merged_config = {**self.default_config, **config}

        return merged_config

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.config.get(key, fallback)

    def load_from_settings_json(self, key: str) -> Any:
        settings_json_path = os.path.expanduser("~/.config/Code/User/settings.json")  # Adjust path as needed
        if os.path.exists(settings_json_path):
            with open(settings_json_path, "r") as f:
                settings = json.load(f)
                return settings.get(key)
        return None
