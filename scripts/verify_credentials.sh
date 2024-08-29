curl --location --request POST 'https://idm.staging.floriday.io/oauth2/ausmw6b47z1BnlHkw0h7/v1/token' \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --data-urlencode 'grant_type=client_credentials' \
     --data-urlencode "client_id=${FLORIDAY_CLIENT_ID}" \
     --data-urlencode "client_secret=${FLORIDAY_CLIENT_SECRET}" \
     --data-urlencode 'scope=role:app catalog:read sales-order:write organization:read supply:read supply:write sales-order:read delivery-conditions:read fulfillment:write fulfillment:read'