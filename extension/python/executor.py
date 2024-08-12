import yaml


class VSCodeAutomation:
    def __init__(
        self,
        yaml_path="run_vscode.yaml",
        progress_file="vscode_extension_progress.json",
    ):
        self.yaml_path = yaml_path
        self.progress_file = progress_file
        self.commands = []

    def add_command(self, command, args=None):
        cmd = {"command": command}
        if args:
            cmd["args"] = args
        self.commands.append(cmd)

    def generate_yaml(self, execute: bool = False):
        config = {"execute": execute, "vscode": self.commands}
        with open(self.yaml_path, "w") as f:
            yaml.dump(config, f)

    def clear_commands(self):
        self.commands = []


def run_vscode_commands(execute):
    automation = VSCodeAutomation(
        yaml_path="run_vscode.yaml",
        progress_file="vscode_extension_progress.json",
    )

    """
    automation.add_command(
        "editor-capture.runUserFriendlyMultiFile",
        ["src/file1.ts, src/file2.js, test/file3.py"],
    )
    """

    # 예시: VSCode 내장 명령어 실행
    automation.add_command("workbench.action.files.save")

    automation.generate_yaml(execute)


if __name__ == "__main__":
    run_vscode_commands(execute=True)
