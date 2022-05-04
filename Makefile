install:
	poetry install

build:
	poetry build

package-install:
	pip install --user dist/*.whl --force-reinstall

page_loader:
	poetry run page_loader

test:
	poetry run pytest -vv

lint:
	poetry run flake8 page_loader

test-coverage:
	poetry run pytest --cov=page_loader tests --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

