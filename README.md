# vine-floriday-adapter

[![Coverage](https://codecov.io/gh/serraict/vine-floriday-adapter/branch/main/graph/badge.svg)](https://codecov.io/gh/serraict/vine-floriday-adapter)

This adapter will make trade information from [Floriday] available on a [Serra Vine] instance of choice.

See the [backlog] to learn what's next and planned.

Contact @serra for suggestions and questions.

## Development

Development done with Python 3.12.2.

Checkout this repository. Then:

```bash
make bootstrap
. ./venv/bin/activate
make update
floridayvine --help
```

Now you can run and debug the command line script `floridayvine`.

### Environment Variable Verification

To verify that all required environment variables are properly defined, use the `verify_env_vars.py` script:

```bash
python scripts/verify_env_vars.py
```

### Testing

This project uses pytest for testing. There are two types of tests:

1. Unit tests: These test individual components and don't require external connections.
2. Integration tests: These test the interaction with Floriday API and the database.

To run tests:

```bash
make test
make test-integration
```

Note: The pre-commit hook does not include running tests. It's important to run tests manually before pushing changes or deploying.

Integration tests require proper setup of the development environment, including correct credentials and connections to Floriday and the database.

## Releasing

To make a release, add a tag like `v0.9.1` and push it.
This type of tag will trigger the [package workflow](./.github/workflows/package.yml).
The application is published as a Docker container to <https://ghcr.io/serraict/vine-floriday-adapter>.

## Usage

For an example of the required environment variables, see [.env.example](.env.example).

When setup, then:

```bash
(venv) ➜  vine-floriday-adapter git:(main) floridayvine db init                                                        
Initializing database on mongodb://root:'*****'@localhost:27017...
Created collection: organizations
Created collection: trade_items
Created collection: supply_lines
(venv) ➜  vine-floriday-adapter git:(main) floridayvine sync status                                          
Max sequence number for organizations: 0
Max sequence number for trade_items: 0
Max sequence number for supply_lines: 0
(venv) ➜  vine-floriday-adapter git:(main) ✗ floridayvine sync organizations  --limit-result 3   
Syncing organizations from 0 to 1164016 ...
Seq nr 864747: Persisting Douwe Hoving | Potplanten ...
Seq nr 864921: Persisting Planten Centrum Twente ...
Seq nr 867216: Persisting VOF van Kester-Duijvesteijn ...
Done syncing organizations
^C
(venv) ➜  vine-floriday-adapter git:(main) ✗ floridayvine sync status                   
Max sequence number for organizations: 867216
Max sequence number for trade_items: 0
Max sequence number for supply_lines: 0
(venv) ➜  vine-floriday-adapter git:(main) ✗ floridayvine sync organizations --start-seq-number 867216 --limit-result 100
[...]
Seq nr 933052: Persisting  ...
Seq nr 933053: Persisting Razek Saliman ...
Done syncing organizations
(venv) ➜  vine-floriday-adapter git:(main) ✗ floridayvine sync supply-lines --limit-result 3
Syncing supply_lines from 0 ...
Seq nr 41059699: Persisting 6584eda4-95ec-4d77-9511-d43348eefade ...
Seq nr 41067630: Persisting c5ce4ec8-35c9-46c1-923f-eac3571599bb ...
Seq nr 41067810: Persisting 24c77740-9103-40a1-9964-49b1be3e00b3 ...
Done syncing supply_lines
```

### As a Python script

Follow the steps in Development.
See the [tests](./tests) directory for example usages.

### As a Container in Serra Vine

See [docker-compose.yml](./docker-compose.yml) for an example to configure the service in Serra Vine.
Your environment variables can be configured in the compose file or in a separate .env file.

---

 [Floriday]: https://www.floriday.io/en/home
 [Serra Vine]: https://vine.serraict.com
 [backlog]: ./work/backlog.md
