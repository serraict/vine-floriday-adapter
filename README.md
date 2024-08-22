# vine-floriday-adapter

This adapter will make trade information from [Floriday] and available on a [Serra Vine] instance of choice.

See the [backlog] to learn what's next and planned.

Contact @serra for suggestions and questions.

## Development

Development done with Python 3.12.2.

Checkout this repository. Then:

```bash
make bootstrap
. ./venv/bin/activate
make update
```

Now you can run and debug the command line script `floridayvine`.

The application is published as a Docker container to <ghcr.io/serraict/vine-floriday-adapter>.
A new container is pushed on each release tag.

## Usage

See the [tests](./tests) directory for example usages.
Or run the following to see all options:

```bash
floridayvine --help
```

Once the files are uploaded to Minio, you can create a virtual dataset in your data lake
as described in this [Serra Learning on formatting a directory as a dataset].

---

 [Floriday]: https://www.floriday.io/en/home
 [Serra Vine]: https://vine.serraict.com
 [backlog]: ./work/backlog.md
 [Serra Learning on formatting a directory as a dataset]: https://serra.fibery.io/Public/Learning/Een-virtuele-dataset-maken-van-een-directory-met-json-bestanden-247?sharing-key=b3769410-f4ab-4926-800e-87e345f535b2