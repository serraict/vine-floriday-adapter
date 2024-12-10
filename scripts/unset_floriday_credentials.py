#!/usr/bin/env python3
"""
Script to unset Floriday-related environment variables.

This script outputs commands to unset the following environment variables:
- FLORIDAY_CLIENT_ID
- FLORIDAY_CLIENT_SECRET
- FLORIDAY_API_KEY

Usage:
    eval $(./scripts/unset_floriday_credentials.py)
"""
import sys


def unset_floriday_credentials():
    """Output commands to unset Floriday-related environment variables."""
    variables_to_unset = [
        "FLORIDAY_CLIENT_ID",
        "FLORIDAY_CLIENT_SECRET",
        "FLORIDAY_API_KEY",
    ]

    for var in variables_to_unset:
        print(f"unset {var}")


if __name__ == "__main__":
    try:
        unset_floriday_credentials()
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
