import subprocess
import os


def run_command(command):
    try:
        env = os.environ.copy()
        env["MINIO_ENDPOINT"] = "dummy_endpoint"
        env["MINIO_ACCESS_KEY"] = "dummy_access_key"
        env["MINIO_SECRET_KEY"] = "dummy_secret_key"
        result = subprocess.run(
            command, capture_output=True, text=True, check=True, env=env
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(command)}: {e}")
        print(f"Stderr: {e.stderr}")
        print(f"Stdout: {e.stdout}")
        return f"Error: Unable to retrieve help for this command.\nStderr: {e.stderr}\nStdout: {e.stdout}"


def generate_documentation():
    # Get the main help output
    main_help = run_command(["floridayvine", "--help"])
    # Parse the main help to get the list of commands
    commands = []
    commands_section = False
    for line in main_help.split("\n"):
        if "Commands" in line and "─" in line:
            commands_section = True
            continue
        if commands_section and "│" in line:
            command = line.split("│")[1].strip().split()[0]
            if command:
                commands.append(command)
        if commands_section and "╰" in line:
            break

    print(f"Found commands: {commands}")

    # Generate the documentation
    doc = "# Floridayvine CLI Documentation\n\n"
    doc += "## Main Command\n\n"
    doc += "```shell\n" + main_help + "```\n\n"

    # Generate documentation for each command
    for command in commands:
        doc += f"## `{command}` Command\n\n"
        command_help = run_command(["floridayvine", command, "--help"])
        doc += "```\n" + command_help + "```\n\n"

    return doc


def main():
    documentation = generate_documentation()
    with open("docs/cli_documentation.md", "w") as f:
        f.write(documentation)
    print("CLI documentation has been generated and saved to docs/cli_documentation.md")


if __name__ == "__main__":
    main()
