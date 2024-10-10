#!/usr/bin/env python3

import os
import sys
import re
import argparse
from dotenv import dotenv_values


def load_env_files(env_path, env_example_path):
    if not os.path.exists(env_path):
        print(f"Error: .env file not found at {env_path}")
        sys.exit(1)
    if not os.path.exists(env_example_path):
        print(f"Error: .env.example file not found at {env_example_path}")
        sys.exit(1)

    env = dotenv_values(env_path)
    env_example = dotenv_values(env_example_path)
    return env, env_example


def extract_used_vars(src_dir):
    used_vars = set()
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    # Look for os.getenv() and os.environ.get() calls
                    matches = re.findall(r'os\.getenv\(["\'](\w+)["\']', content)
                    matches += re.findall(r'os\.environ\.get\(["\'](\w+)["\']', content)
                    used_vars.update(matches)
    return used_vars


def compare_vars(env, env_example, used_vars):
    missing_vars = set(used_vars) - set(env_example.keys())
    extra_vars = set(env_example.keys()) - set(used_vars)
    return missing_vars, extra_vars


def main(env_path, env_example_path, src_dir):
    env, env_example = load_env_files(env_path, env_example_path)
    used_vars = extract_used_vars(src_dir)
    missing_vars, extra_vars = compare_vars(env, env_example, used_vars)

    print(f"Variables found in the application ({src_dir}):")
    for var in sorted(used_vars):
        print(f"  - {var}")

    print(f"\nVariables in {env_example_path}:")
    for var in sorted(env_example.keys()):
        print(f"  - {var}")

    if missing_vars:
        print(
            f"\nError: The following variables are used in the application but not defined in {env_example_path}:"
        )
        for var in sorted(missing_vars):
            print(f"  - {var}")
        print(
            f"\nPlease add these variables to {env_example_path} with appropriate default values."
        )
        sys.exit(1)

    if extra_vars:
        print(
            f"\nWarning: The following variables are defined in {env_example_path} but not used in the application:"
        )
        for var in sorted(extra_vars):
            print(f"  - {var}")
        print("\nConsider removing these variables if they are no longer needed.")

    if not missing_vars and not extra_vars:
        print("\nAll environment variables are correctly defined and used.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Verify environment variables in a Python project."
    )
    parser.add_argument("--env", default=".env", help="Path to the .env file")
    parser.add_argument(
        "--env-example", default=".env.example", help="Path to the .env.example file"
    )
    parser.add_argument("--src", default="src", help="Path to the source directory")
    args = parser.parse_args()

    main(args.env, args.env_example, args.src)
