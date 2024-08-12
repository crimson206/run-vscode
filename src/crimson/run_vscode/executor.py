import yaml
import os
from typing import Any


class VSCodeAutomation:
    def __init__(
        self,
        yaml_path: str = "temp/run_vscode/run_vscode.yaml",
        progress_file: str = "temp/run_code/vscode_extension_progress.json",
    ):
        self.yaml_path = yaml_path
        self.progress_file = progress_file
        self.commands = []

    def add_command(self, command: str, args: Any = None):
        cmd = {"command": command}
        if args:
            cmd["args"] = args
        self.commands.append(cmd)

    def generate_yaml(self, execute: bool = False):
        config = {"execute": execute, "vscode": self.commands}

        directory = os.path.dirname(self.yaml_path)

        if not os.path.exists(directory):
            os.makedirs(directory)

        # YAML 파일 작성
        with open(self.yaml_path, "w") as f:
            yaml.dump(config, f)

    def clear_commands(self):
        self.commands = []
