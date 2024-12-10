#!/usr/bin/env python3
"""
Script to load Floriday credentials from a 1Password vault.

This script uses the 1Password CLI (op) to fetch and set the following environment variables:
- FLORIDAY_CLIENT_ID
- FLORIDAY_CLIENT_SECRET
- FLORIDAY_API_KEY

Usage:
    ./scripts/load_floriday_credentials.py VAULT_NAME

Example:
    ./scripts/load_floriday_credentials.py Development
"""
import argparse
import os
import subprocess
import sys
import json


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


def load_floriday_credentials(vault: str):
    """Load Floriday credentials from 1Password and set environment variables."""
    print(f"Loading Floriday credentials from vault: {vault}")

    # Fetch credentials from 1Password
    item_data = run_op_command(vault, "Floriday Staging")

    # Extract and set environment variables
    credentials = {
        "FLORIDAY_CLIENT_ID": "CLIENT_ID",
        "FLORIDAY_CLIENT_SECRET": "CLIENT_SECRET",
        "FLORIDAY_API_KEY": "API_KEY",
    }

    for env_var, field_name in credentials.items():
        value = get_field_value(item_data, field_name)
        os.environ[env_var] = value
        print(f"Set {env_var}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Load Floriday credentials from a 1Password vault"
    )
    parser.add_argument(
        "vault", help="Name of the 1Password vault containing Floriday credentials"
    )

    args = parser.parse_args()

    # Check if op CLI is available
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

    load_floriday_credentials(args.vault)


if __name__ == "__main__":
    main()
