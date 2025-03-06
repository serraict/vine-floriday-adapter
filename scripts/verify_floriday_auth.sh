#!/bin/bash

# Script to verify Floriday authentication using the example curl calls from the documentation

echo "Floriday Authentication Verification Script"
echo "========================================"
echo

# Check if required environment variables are set
if [ -z "$FLORIDAY_CLIENT_ID" ] || [ -z "$FLORIDAY_CLIENT_SECRET" ] || [ -z "$FLORIDAY_API_KEY" ] || [ -z "$FLORIDAY_AUTH_URL" ] || [ -z "$FLORIDAY_BASE_URL" ]; then
    echo "Error: Missing required environment variables."
    echo "Please ensure FLORIDAY_CLIENT_ID, FLORIDAY_CLIENT_SECRET, FLORIDAY_API_KEY, FLORIDAY_AUTH_URL, and FLORIDAY_BASE_URL are set."
    exit 1
fi

echo "Step 1: Requesting a token..."
token_response=$(curl --silent --location --request POST "$FLORIDAY_AUTH_URL" \
    --header 'Accept: application/json' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode "client_id=$FLORIDAY_CLIENT_ID" \
    --data-urlencode "client_secret=$FLORIDAY_CLIENT_SECRET" \
    --data-urlencode 'scope=role:app catalog:read sales-order:write organization:read supply:read supply:write sales-order:read delivery-conditions:read fulfillment:write fulfillment:read')

# Check if the token request was successful and extract the token
if [[ "$token_response" == *"access_token"* ]]; then
    echo "Successfully obtained an access token."
    access_token=$(echo "$token_response" | grep -o '"access_token":"[^"]*' | sed 's/"access_token":"//')
    
    echo
    echo "Step 2: Testing API access with the token..."
    
    api_response=$(curl --silent --location --request GET "$FLORIDAY_BASE_URL/auth/key" \
        --header "X-Api-Key: $FLORIDAY_API_KEY" \
        --header 'Accept: application/json' \
        --header "Authorization: Bearer $access_token")
    
    # Check if the API request was successful
    if [[ "$api_response" == *"apiVersion"* ]] || [[ "$api_response" == *"organizationId"* ]]; then
        echo "Successfully accessed the API."
        echo "Authentication verification completed successfully."
    else
        echo "Failed to access the API."
        echo "Please check your API key and token."
        exit 1
    fi
else
    echo "Failed to obtain an access token."
    echo "Please check your client ID and client secret."
    exit 1
fi
