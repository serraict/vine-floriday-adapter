#!/usr/bin/env python3
"""
Script to manage Floriday credentials using 1Password.

This script provides commands to:
1. Load credentials from a 1Password vault
2. Unset credentials from the environment

Usage:
    # Load credentials
    eval $(./scripts/floriday_credentials.py load "Serra Vine")

    # Unset credentials
    eval $(./scripts/floriday_credentials.py unset)
"""
import subprocess
import sys
import json
import typer

app = typer.Typer(help="Manage Floriday credentials")


def run_op_command(vault: str, item_name: str) -> dict:
    """Run 1Password CLI command to get item details."""
    try:
        result = subprocess.run(
            ["op", "item", "get", item_name, "--vault", vault, "--format", "json"],
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error accessing 1Password: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error parsing 1Password output", file=sys.stderr)
        sys.exit(1)


def get_field_value(item_data: dict, field_name: str) -> str:
    """Extract field value from 1Password item data."""
    for field in item_data.get("fields", []):
        if field.get("label") == field_name:
            return field.get("value", "")
    print(f"Field '{field_name}' not found in 1Password item", file=sys.stderr)
    sys.exit(1)


def check_op_version():
    """Check if op CLI is available with correct version."""
    try:
        version = subprocess.run(
            ["op", "--version"], capture_output=True, text=True, check=True
        )
        if not version.stdout.startswith("2.30"):
            print(
                "Warning: This script was designed for op CLI version 2.30",
                file=sys.stderr,
            )
    except subprocess.CalledProcessError:
        print("Error: 1Password CLI (op) not found or not accessible", file=sys.stderr)
        sys.exit(1)


@app.command()
def load(
    vault: str = typer.Argument(
        ..., help="Name of the 1Password vault containing Floriday credentials"
    )
):
    """Load Floriday credentials from 1Password and output export commands."""
    check_op_version()

    # Fetch credentials from 1Password
    item_data = run_op_command(vault, "Floriday Staging")

    # Extract and print export commands
    credentials = {
        "FLORIDAY_CLIENT_ID": "CLIENT_ID",
        "FLORIDAY_CLIENT_SECRET": "CLIENT_SECRET",
        "FLORIDAY_API_KEY": "API_KEY",
    }

    for env_var, field_name in credentials.items():
        value = get_field_value(item_data, field_name)
        print(f"export {env_var}='{value}'")


@app.command()
def unset():
    """Output commands to unset Floriday-related environment variables."""
    variables = [
        "FLORIDAY_CLIENT_ID",
        "FLORIDAY_CLIENT_SECRET",
        "FLORIDAY_API_KEY",
    ]

    for var in variables:
        print(f"unset {var}")


if __name__ == "__main__":
    app()
