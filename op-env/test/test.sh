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

# Create temporary .env.example
TEMP_ENV_EXAMPLE=$(mktemp)
trap 'rm -f "$TEMP_ENV_EXAMPLE"' EXIT

echo "Setting up test environment..."
cat > "$TEMP_ENV_EXAMPLE" << EOL
TEST_VAR_1=value1
TEST_VAR_2=value2
TEST_VAR_NOT_IN_VAULT=value3
EOL

# Function to run tests
run_test() {
    local test_name="$1"
    local command="$2"
    local expected_output="$3"
    local actual_output
    
    echo "Running test: $test_name"
    actual_output=$($command)
    
    if [[ "$actual_output" == *"$expected_output"* ]]; then
        echo "✓ Test passed"
    else
        echo "✗ Test failed"
        echo "Expected output to contain: $expected_output"
        echo "Actual output: $actual_output"
        exit 1
    fi
}

# Test direct execution (should fail)
echo "Testing direct execution..."
if $OP_ENV 2>&1 | grep -q "must be sourced"; then
    echo "✓ Direct execution test passed"
else
    echo "✗ Direct execution test failed"
    exit 1
fi

# Create a test shell to source the script
TEST_SHELL=$(mktemp)
trap 'rm -f "$TEST_SHELL"' EXIT

# Test load command
cat > "$TEST_SHELL" << EOL
#!/usr/bin/env bash
source "$OP_ENV" load "$VAULT" "$ITEM"
EOL
chmod +x "$TEST_SHELL"

echo "Testing load command..."
if output=$($TEST_SHELL) && [[ "$output" == *"Set"* ]]; then
    echo "✓ Load test passed"
else
    echo "✗ Load test failed"
    echo "Output: $output"
    exit 1
fi

# Test unset command
cat > "$TEST_SHELL" << EOL
#!/usr/bin/env bash
source "$OP_ENV" unset "$VAULT" "$ITEM"
EOL

echo "Testing unset command..."
if output=$($TEST_SHELL) && [[ "$output" == *"Unset"* ]]; then
    echo "✓ Unset test passed"
else
    echo "✗ Unset test failed"
    echo "Output: $output"
    exit 1
fi

# Test missing arguments
cat > "$TEST_SHELL" << EOL
#!/usr/bin/env bash
source "$OP_ENV" load
EOL

echo "Testing missing arguments..."
if output=$($TEST_SHELL 2>&1) && [[ "$output" == *"Both vault name and item name are required"* ]]; then
    echo "✓ Missing arguments test passed"
else
    echo "✗ Missing arguments test failed"
    echo "Output: $output"
    exit 1
fi

echo "All tests passed! 🎉"
