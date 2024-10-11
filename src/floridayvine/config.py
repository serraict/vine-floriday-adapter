import os
import sys


def check_environment_variables():
    required_vars = [
        "FLORIDAY_CLIENT_ID",
        "FLORIDAY_CLIENT_SECRET",
        "FLORIDAY_AUTH_URL",
        "FLORIDAY_BASE_URL",
        "FLORIDAY_API_KEY",
        "MONGODB_CONNECTION_STRING",
    ]
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
        print(f"Environment variable {var}: {'[SET]' if value else '[NOT SET]'}")

    if missing_vars:
        print(
            f"Error: Missing required environment variables: {', '.join(missing_vars)}"
        )
        print("Please set these variables before running the application.")
        print("For more information, refer to the project documentation:")
        print("https://github.com/serraict/vine-floriday-adapter#readme")
        sys.exit(1)


# Run the check when this module is imported
check_environment_variables()
