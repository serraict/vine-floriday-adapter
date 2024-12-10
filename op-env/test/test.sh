#!/usr/bin/env bash
# Test script for op-env
#
# Usage:
#   ./test.sh VAULT_NAME ITEM_NAME

set -e  # Exit on error

# Check arguments
if [ "$#" -ne 2 ]; then
    echo "Error: Both vault name and item name are required"
    echo "Usage: $0 VAULT_NAME ITEM_NAME"
    exit 1
fi

VAULT="$1"
ITEM="$2"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OP_ENV="${SCRIPT_DIR}/../bin/op-env"
TEST_DIR=$(mktemp -d)
trap 'rm -rf "$TEST_DIR"' EXIT

# Create test environment
echo "Setting up test environment..."
cd "$TEST_DIR"

cat > .env.example << EOL
FLORIDAY_CLIENT_ID=your_client_id
FLORIDAY_CLIENT_SECRET=your_client_secret
FLORIDAY_API_KEY=your_api_key
FLORIDAY_AUTH_URL=https://example.com
EOL

# Test direct execution (should fail)
echo "Testing direct execution..."
if $OP_ENV 2>&1 | grep -q "must be sourced"; then
    echo "✓ Direct execution test passed"
else
    echo "✗ Direct execution test failed"
    exit 1
fi

# Create a test shell to source the script
TEST_SHELL="$TEST_DIR/test_shell.sh"

# Test load command
cat > "$TEST_SHELL" << EOL
#!/usr/bin/env bash
cd "$TEST_DIR"
source "$OP_ENV" load "$VAULT" "$ITEM"
EOL
chmod +x "$TEST_SHELL"

echo "Testing load command..."
if output=$("$TEST_SHELL") && [[ "$output" == *"Set FLORIDAY_CLIENT_ID"* ]]; then
    echo "✓ Load test passed"
else
    echo "✗ Load test failed"
    echo "Output: $output"
    exit 1
fi

# Test unset command
cat > "$TEST_SHELL" << EOL
#!/usr/bin/env bash
cd "$TEST_DIR"
source "$OP_ENV" unset "$VAULT" "$ITEM"
EOL

echo "Testing unset command..."
if output=$("$TEST_SHELL") && [[ "$output" == *"Unset FLORIDAY_CLIENT_ID"* ]]; then
    echo "✓ Unset test passed"
else
    echo "✗ Unset test failed"
    echo "Output: $output"
    exit 1
fi

# Test missing arguments
echo "Testing missing arguments..."
cat > "$TEST_SHELL" << EOL
#!/usr/bin/env bash
cd "$TEST_DIR"
source "$OP_ENV" load
if [[ "\$?" -eq 1 ]]; then
    exit 0
else
    exit 1
fi
EOL

if "$TEST_SHELL"; then
    echo "✓ Missing arguments test passed"
else
    echo "✗ Missing arguments test failed"
    exit 1
fi

echo "All tests passed! 🎉"
