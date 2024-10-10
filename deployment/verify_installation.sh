#!/bin/bash

echo "Verifying floridayvine installation..."

# Test Floriday API connection
echo "Testing Floriday API connection..."
if docker exec floridayvine floridayvine floriday floriday-connection-info; then
    echo "Floriday API connection successful."
else
    echo "Error: Unable to connect to Floriday API."
    exit 1
fi

echo "Installation verification complete. All checks passed."
