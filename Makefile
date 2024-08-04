# Set default variables
PACKAGE_NAME ?= report

# Declare phony targets
.PHONY: lint format test

# Linting
lint:
	@mypy $(PACKAGE_NAME)
	@ruff $(PACKAGE_NAME)

# Formatting
format:
	@isort $(PACKAGE_NAME)
	@black $(PACKAGE_NAME)

# Run local tests
test:
	@pytest -s -p no:warnings \
		--maxfail 1 \
		--cov-report=term-missing:skip-covered \
		--cov=reporter \
		-v tests