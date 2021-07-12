.PHONY: help
help: ## Help
	@echo "Usage:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-15s\033[0m %s\n", $$1, $$2}'

env: ## Create a virtualenv environment
	# Create venv directory if not exist
	test -d env || virtualenv env
	./env/bin/python -m pip install -r requirements.txt

dev-env: env ## Create a development virtualenv environment
	./env/bin/python -m pip install -r requirements-dev.txt

.PHONY: test
test: dev-env unit-tests functional-tests ## Create dev env, run linter and run all tests

linter: ## Run linter
	./env/bin/flake8 tests functional_tests

unit-tests:  ## Run unit test
	find . -name '*.pyc' -exec rm -f {} \;
	./env/bin/python -m pytest \
	    --doctest-modules \
	    --disable-warnings \
	    --verbose \
	    app tests

functional-tests: run kill-server ## Run functional test
	./env/bin/python -m unittest functional_tests/tests.py

kill-server:
	@lsof -ti :5000 | xargs kill

run: ## Run development server
	export FLASK_ENV=development; \
	export FLASK_APP=app; \
	flask run &

package: ## Package application
	python setup.py sdist

clean: ## Clean build
	rm -rf build dist nlp.egg-info
