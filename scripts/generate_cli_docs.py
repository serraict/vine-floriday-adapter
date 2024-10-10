import importlib
import inspect
import os
import typer
from typing import Dict, Any, Union


def import_commands():
    commands = {}
    commands_dir = os.path.join("src", "floridayvine", "commands")
    for filename in os.listdir(commands_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = f"floridayvine.commands.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for name, obj in inspect.getmembers(module):
                if isinstance(obj, typer.Typer):
                    commands[filename[:-3]] = obj
    return commands


def get_command_help(command: Union[typer.Typer, typer.models.CommandInfo]) -> str:
    if isinstance(command, typer.Typer):
        return command.info.help if command.info and command.info.help else ""
    elif isinstance(command, typer.models.CommandInfo):
        return command.help if command.help else ""
    return ""


def get_subcommands(command: Union[typer.Typer, typer.models.CommandInfo]) -> list:
    if isinstance(command, typer.Typer):
        return [
            cmd
            for cmd in command.registered_commands
            if cmd.name and cmd.name != "None" and not cmd.name.startswith("_")
        ]
    return []


def document_command(
    command: Union[typer.Typer, typer.models.CommandInfo], name: str, indent: str = ""
) -> str:
    md_content = f"{indent}### `{name}`\n\n"

    help_text = get_command_help(command)
    if help_text:
        md_content += f"{indent}{help_text}\n\n"

    md_content += f"{indent}#### Usage\n\n"
    md_content += f"{indent}```\n"
    md_content += f"{indent}floridayvine {name} [OPTIONS] [ARGS]...\n"
    md_content += f"{indent}```\n\n"

    # Document options
    if isinstance(command, typer.Typer) and command.registered_callback:
        md_content += document_options(command.registered_callback, indent)
    elif isinstance(command, typer.models.CommandInfo):
        md_content += document_options(command, indent)
    else:
        md_content += f"{indent}#### Options\n\n"
        md_content += f"{indent}This command has no options.\n\n"

    subcommands = get_subcommands(command)
    if subcommands:
        md_content += f"{indent}#### Subcommands\n\n"
        for subcommand in subcommands:
            subcommand_help = get_command_help(subcommand)
            md_content += f"{indent}- `{subcommand.name}`"
            if subcommand_help:
                md_content += f": {subcommand_help}"
            md_content += "\n"
        md_content += "\n"

        for subcommand in subcommands:
            md_content += document_command(
                subcommand, f"{name} {subcommand.name}", indent + "  "
            )
    else:
        md_content += f"{indent}*This command has no subcommands.*\n\n"

    md_content += (
        f"{indent}For more detailed information, use `floridayvine {name} --help`.\n\n"
    )

    return md_content


def document_options(callback: Any, indent: str = "") -> str:
    md_content = f"{indent}#### Options\n\n"
    params = callback.params if hasattr(callback, "params") else []
    if not params:
        md_content += f"{indent}This command has no options.\n\n"
        return md_content
    for param in params:
        option_str = f"{indent}- `"
        if param.opts:
            option_str += ", ".join(param.opts)
        option_str += "`"
        if param.help:
            option_str += f": {param.help}"
        if param.default is not None and not callable(param.default):
            option_str += f" (default: {param.default})"
        md_content += f"{option_str}\n"
    md_content += "\n"
    return md_content


def generate_markdown(commands: Dict[str, typer.Typer]) -> str:
    md_content = "# Floridayvine CLI Documentation\n\n"
    md_content += "This document provides an overview of the Floridayvine CLI application and its commands.\n\n"

    md_content += "## Usage\n\n"
    md_content += "```\n"
    md_content += "floridayvine [OPTIONS] COMMAND [ARGS]...\n"
    md_content += "```\n\n"

    md_content += "## Global Options\n\n"
    md_content += "- `--help`: Show this message and exit.\n\n"

    md_content += "## Commands\n\n"

    for command_name, command in commands.items():
        md_content += document_command(command, command_name)

    md_content += "Note: This documentation is automatically generated. Some commands may have additional options or subcommands not captured here. Always use the `--help` option with any command for the most up-to-date and detailed information.\n"

    return md_content


def main():
    commands = import_commands()
    md_content = generate_markdown(commands)
    with open("docs/cli_documentation.md", "w") as f:
        f.write(md_content)
    print("CLI documentation has been generated and saved to docs/cli_documentation.md")


if __name__ == "__main__":
    main()
