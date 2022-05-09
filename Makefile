install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

page_loader:
	poetry run page_loader

publish:
	poetry publish --dry-run

test:
	poetry run pytest -vv

lint:
	poetry run flake8 page_loader

test-coverage:
	poetry run pytest --cov=page_loader tests --cov-report xml

selfcheck:
	poetry check

build: check
	poetry build

check: selfcheck test lint
