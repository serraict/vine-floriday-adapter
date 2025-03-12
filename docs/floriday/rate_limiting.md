# Rate limiting

> This is the auth documentation as retrieved on Mar 3, 2025.

- Rate limits are implemented to ensure optimal performance for all Floriday users;
- Rate limits apply to each connected API key;
- The exact rate limits are mentioned in the Swagger pages and specified per endpoint;
- Currently, most endpoints are limited to 3.4 calls per second (204 per minute) with a burst limit of 1000;
- When deemed necessary, Floriday reserves the right to adjust the rate limits of Endpoints to guarantee the best operation of the platform;
- Users will be notified when rate limits are adjusted in the known Slack channels.
- When deemed necessary (i.e. in case of abuse), Floriday reserves the right to temporarily block an endpoint for an organization or client.