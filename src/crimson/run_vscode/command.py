import argparse
from .executor import VSCodeAutomation


def command_main():
    parser = argparse.ArgumentParser(
        description="Run VS Code commands from the terminal."
    )
    parser.add_argument("command", help="The VS Code command to execute.")
    args = parser.parse_args()

    # Initialize your VSCodeAutomation instance
    automation = VSCodeAutomation(config_filename='.run_vscode')

    # Add the command to the automation
    automation.add_command(args.command)

    # Generate the YAML (execute=False to not run immediately)
    automation.generate_yaml(execute=True)

    # You can add logic to execute it immediately if needed
    # For example, calling a method on automation to trigger the command directly
    print(f"Command {args.command} executed.")


if __name__ == "__main__":
    command_main()
