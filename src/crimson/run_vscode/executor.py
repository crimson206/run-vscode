import yaml
import os
from typing import Any, Optional


class VSCodeAutomation:
    def __init__(self, config_filename: str = ".run_vscode"):
        self.yaml_path = None
        self.progress_file = None
        self.output_dir = "temp/run_vscode"
        self.commands = []
        self.load_config(config_filename)

    def find_config_file(self, filename: str) -> Optional[str]:
        """Search for the configuration file by traversing up the directory tree."""
        current_dir = os.getcwd()

        while current_dir != os.path.dirname(
            current_dir
        ):  # Continue until we reach the root directory
            potential_path = os.path.join(current_dir, filename)
            if os.path.exists(potential_path):
                return potential_path
            current_dir = os.path.dirname(current_dir)  # Move up one directory

        return None

    def load_config(self, config_filename: str):
        config_file_path = self.find_config_file(config_filename)

        if config_file_path:
            with open(config_file_path, "r") as f:
                config = yaml.safe_load(f)
                self.yaml_path = config.get(
                    "yaml_path", f"{self.output_dir}/run_vscode.yaml"
                )
                self.progress_file = config.get(
                    "progress_file", f"{self.output_dir}/vscode_extension_progress.json"
                )
        else:
            # Default paths if no config file is found
            self.yaml_path = f"{self.output_dir}/run_vscode.yaml"
            self.progress_file = f"{self.output_dir}/vscode_extension_progress.json"

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

        # Write YAML file
        with open(self.yaml_path, "w") as f:
            yaml.dump(config, f)

    def clear_commands(self):
        self.commands = []
