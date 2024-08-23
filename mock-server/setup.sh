npm install -g @stoplight/prism-cli
curl -o swagger.json https://api.staging.floriday.io/suppliers-api-2024v1/swagger/UUID/swagger.json
prism mock swagger.json --port 9876
curl http://localhost:9876/additional-services
curl -H "Accept: application/json" http://127.0.0.1:9876/weekly-supply-line-counters