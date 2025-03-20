.PHONY: clean-pyc clean-build docs clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "test - run tests on every Python version with tox"
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

test:
	tox

docs:
	rm -f docs/fuzzyfinder.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ fuzzyfinder
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html
