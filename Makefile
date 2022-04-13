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