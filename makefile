.phony : all

bootstrap:
	python -m venv venv
	mkdir -p ./output
	mkdir -p ./output/specs	
	@echo "Run 'source venv/bin/activate' to activate the virtual environment, followed by 'make update' to install dependencies."
update:
	python -m pip install --upgrade pip build
	python -m pip install -r requirements-dev.txt
	pip install -e .
console:
test:
	pytest
build:
	python -m build
documentation:
printversion:
	@python -m setuptools_scm
release:
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
	@git tag v$$(python -m setuptools_scm --strip-dev)
	@git push origin --tags