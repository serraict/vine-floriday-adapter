# op-env

A shell script to manage environment variables using 1Password.

## Features

- Reads variable names from `.env.example`
- Only manages variables that exist in 1Password
- Uses `source` to properly modify shell environment
- Never exposes sensitive values in output
- Verifies 1Password CLI version
- Clear error handling and feedback

## Requirements

- 1Password CLI (op) version 2.30 or higher
- A `.env.example` file in your project listing the environment variables
- Bash shell

## Installation

1. Copy the `op-env` directory to your project or a central location
2. Add the `op-env/bin` directory to your PATH (optional)

## Usage

The script must be sourced (not executed) to modify environment variables:

```bash
# Load variables from 1Password
source ./op-env/bin/op-env load "Your Vault" "Your Item"

# Unset variables that exist in 1Password
source ./op-env/bin/op-env unset "Your Vault" "Your Item"
```

### Example

Given a `.env.example` file:
```
API_KEY=your_api_key
CLIENT_ID=your_client_id
DEBUG=true
BASE_URL=http://localhost:3000
```

And a 1Password item containing `API_KEY` and `CLIENT_ID`, running:
```bash
source ./op-env/bin/op-env load "My Vault" "Project Secrets"
```

Will:
- Set `API_KEY` and `CLIENT_ID` from 1Password
- Ignore `DEBUG` and `BASE_URL` (not in 1Password)
- Show which variables were set/ignored

## Testing

Run the test script to verify functionality:
```bash
./op-env/test/test.sh "Your Vault" "Your Item"
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use this in your projects!
