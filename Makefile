install:
	poetry install

build:
	poetry build

package-install:
	pip install --user dist/*.whl --force-reinstall

page_loader:
	poetry run page_loader

test:
	poetry run pytest

lint:
	poetry run flake8 page_loader

selfcheck:
	poetry check
test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml
check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
