npm install -g @stoplight/prism-cli
curl -o swagger.json https://api.staging.floriday.io/suppliers-api-2024v1/swagger/UUID/swagger.json
prism mock swagger.json --port 9876