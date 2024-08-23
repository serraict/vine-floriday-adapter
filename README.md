# vine-floriday-adapter

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

## Releasing

To make a release, add a tag like `v0.9.1` and push it.
This type of tag will trigger the [package workflow](./.github/workflows/package.yml).
The application is published as a Docker container to <https://ghcr.io/serraict/vine-floriday-adapter>.


## Usage

### As a Python script

Follow the steps in Development.
See the [tests](./tests) directory for example usages.

Once the files are uploaded to Minio, you can create a virtual dataset in your data lake
as described in this [Serra Learning on formatting a directory as a dataset].

### As a Container in Serra Vine

See [docker-compose.yml](./docker-compose.yml) for an example to configure the service in Serra Vine.
Your environment variables can be configured in the compose file or in a separate env file.

---

 [Floriday]: https://www.floriday.io/en/home
 [Serra Vine]: https://vine.serraict.com
 [backlog]: ./work/backlog.md
 [Serra Learning on formatting a directory as a dataset]: https://serra.fibery.io/Public/Learning/Een-virtuele-dataset-maken-van-een-directory-met-json-bestanden-247?sharing-key=b3769410-f4ab-4926-800e-87e345f535b2