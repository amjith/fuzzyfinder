.PHONY: help clean clean-build clean-pyc clean-test test docs

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test, coverage and formatting artifacts"
	@echo "test - run tests with tox and format with ruff"
	@echo "docs - generate Sphinx HTML documentation, including API docs"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	# Directory .tox/, if it exists, contains subdirectories ending with
	# "egg", so we need to exclude it from the search.
	find . -name '*.egg' -prune -name ".tox" -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache/
	rm -fr .ruff_cache/

test:
	tox

docs:
	sphinx-apidoc -o docs/ fuzzyfinder
	rm docs/modules.rst
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html
