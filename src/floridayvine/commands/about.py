import typer
from importlib.metadata import version as get_package_version
from pprint import pprint
from pymongo import MongoClient
from ..persistence import (
    masked_connection_string,
    mongodb_connection_string,
    check_database_status,
)
from ..floriday.auth import get_auth_info, BASE_URL
from ..floriday.api_client import get_api_client

app = typer.Typer(
    invoke_without_command=True,
    help="Display information about the Floriday Vine command line interface.",
)


def get_version():
    return get_package_version("floridayvine")


def check_api_version():
    """
    Check if the API version in the base URL matches the expected version.

    Returns:
        None if the version is correct, or an error message if there's a mismatch.
    """
    try:
        get_api_client()
        return None
    except ValueError as e:
        return str(e)


def check_database_connection():
    if not mongodb_connection_string:
        return "MONGODB_CONNECTION_STRING environment variable is not set."

    try:
        client = MongoClient(mongodb_connection_string, serverSelectionTimeoutMS=5000)
        # Try to get server info
        server_info = client.server_info()

        # Check database status
        db_status, db_message = check_database_status()

        if db_status:
            return f"Successfully connected to the database at {masked_connection_string}. Server version: {server_info.get('version', 'Unknown')}. {db_message}"
        else:
            return f"""Connected to the database at {masked_connection_string}, but there are issues:

            {db_message}.

            Please run 'floridayvine db init' to set up the database properly."""
    except Exception as e:
        return f"Failed to connect to the database at {masked_connection_string}. Error: {str(e)}"


@app.callback()
def callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        show_info()


@app.command()
def version():
    """
    Display the current version of Floriday Vine.
    """
    print(f"{get_version()}")


@app.command()
def show_info():
    """
    Display information about Floriday Vine, its connection to Floriday, and database status.
    """
    print(
        "Floriday Vine is a Python package to ingest Floriday trade information into Serra Vine."
    )
    print(f"Version: {get_version()}")

    print("\nDatabase Connection Status:")
    print(check_database_connection())

    print("\nFloriday Connection Status:")

    # Display the base URL
    if not BASE_URL:
        print("WARNING: FLORIDAY_BASE_URL environment variable is not set.")
    else:
        print(f"Using Floriday API base URL: {BASE_URL}")

    # Check API version
    version_error = check_api_version()
    if version_error:
        print("WARNING: API version mismatch detected!")
        print(version_error)

    try:
        orgs = get_auth_info()
        print("Successfully connected to Floriday.")
        print("Organizations:")
        pprint(orgs)
    except Exception as e:
        print(f"Failed to connect to Floriday. Error: {str(e)}")
        print("For troubleshooting, please refer to the project documentation:")
        print("https://github.com/serraict/vine-floriday-adapter#readme")


if __name__ == "__main__":
    app()
