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
    missing_vars = [var for var in required_vars if not os.getenv(var)]

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
