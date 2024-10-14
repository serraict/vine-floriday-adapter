.phony : all

VERSION := $(shell git describe --tags)
ifeq ($(VERSION),)
    VERSION := v0.0.1
endif

bootstrap:
	python -m venv venv
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip build
	python -m pip install -r requirements-dev.txt
	pip install -e .
console:
test:
	pytest -m "not integration"
test-integration:
	pytest -m "integration"
build:
	python -m build
documentation:
	python scripts/generate_cli_docs.py
printversion:
	@python -m setuptools_scm
release: documentation
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "There are uncommitted changes or untracked files"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then \
		echo "Not on main branch"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse HEAD)" != "$$(git rev-parse origin/main)" ]; then \
		echo "Local branch is ahead of origin"; \
		exit 1; \
	fi
	@NEW_VERSION=$$(python -m setuptools_scm --strip-dev) && \
	sed -i '' "s/\[Unreleased\]/[$${NEW_VERSION}] - $$(date +%Y-%m-%d)/" CHANGELOG.md && \
	if [ -n "$$(git status --porcelain CHANGELOG.md)" ]; then \
		git add CHANGELOG.md && \
		git commit -m "Update CHANGELOG.md for version $${NEW_VERSION}"; \
	fi
	git tag v$${NEW_VERSION} && \
	git push origin main --tags
docker_image:
	docker build -t ghcr.io/serraict/vine-floriday-adapter:$(VERSION) .
docker_push: docker_image
	docker push ghcr.io/serraict/vine-floriday-adapter:$(VERSION)
docker_compose_debug:
	docker compose up --build
mongodb:
	docker compose -f mongodb-docker-compose.yml up
mongodb_bg:
	docker compose -f mongodb-docker-compose.yml up -d
stop_mongodb:
	docker compose -f mongodb-docker-compose.yml down

quality:
	@echo "Running code quality checks..."
	flake8 src tests
	black --check src tests
	pre-commit run --all-files
	@echo "Running tests..."
	pytest -m "not integration"
	@echo "Code quality checks completed."
