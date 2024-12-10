#!/usr/bin/env python3
"""
Script to unset Floriday-related environment variables.

This script removes the following environment variables:
- FLORIDAY_CLIENT_ID
- FLORIDAY_CLIENT_SECRET
- FLORIDAY_API_KEY

Usage:
    python scripts/unset_floriday_credentials.py
    # or after making executable:
    ./scripts/unset_floriday_credentials.py
"""
import os
import sys


def unset_floriday_credentials():
    """Unset Floriday-related environment variables."""
    variables_to_unset = [
        "FLORIDAY_CLIENT_ID",
        "FLORIDAY_CLIENT_SECRET",
        "FLORIDAY_API_KEY",
    ]

    for var in variables_to_unset:
        if var in os.environ:
            del os.environ[var]
            print(f"Unset {var}")
        else:
            print(f"{var} was not set")


if __name__ == "__main__":
    try:
        unset_floriday_credentials()
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
