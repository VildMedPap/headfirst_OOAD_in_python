.DEFAULT_GOAL := %

# Virtual environment paths
VIRTUAL_ENV_NAME := .venv

# Directories
ROOT_DIR := $(CURDIR)
CACHE_DIR := $(ROOT_DIR)/.cache
PKG_DIR := $(ROOT_DIR)/src
TEST_DIR := $(ROOT_DIR)/tests

#------------------#
#   MISC TARGETS   #
#------------------#

.PHONY: %

%:
	@echo "Target $@ is not defined. Running help target instead:\n"

#-------------------#
#   SETUP TARGETS   #
#-------------------#

.PHONY: install create-environment install-dependencies

install: create-environment $(TOOLS_FIRST_INSTALLED) install-dependencies ## Setup environment and install all dependencies

create-environment:
	@pyenv install --skip-existing $(shell cat $(ROOT_DIR)/.python-version)
	@poetry env use -- $(shell pyenv which python)
	@mkdir -p $(CACHE_DIR)/mypy

install-dependencies:
	@poetry install --with dev

#----------------------#
#   TEARDOWN TARGETS   #
#----------------------#

.PHONY: teardown rm-lock rm-venv rm-cache

teardown: rm-lock rm-venv rm-cache ## Remove .venv, .cache, poetry.lock, etc.

rm-lock:
	@rm -rf poetry.lock

rm-venv:
	@rm -rf $(VIRTUAL_ENV_NAME)

rm-cache:
	@rm -rf $(CACHE_DIR)

#----------------#
#   CI TARGETS   #
#----------------#

.PHONY: ci linting test test-slow

ci: linting test-slow ## Emulate CI pipeline (linters and tests)

test: ## Run test suite
	@poetry run pytest -m "not slow" $(TEST_DIR)

test-slow: ## Run test suite
	@poetry run pytest $(TEST_DIR)

#---------------------#
#   LINTERS TARGETS   #
#---------------------#

.PHONY: linting ruff mypy

linting: ruff mypy ## Run all linters

ruff:
	@poetry run ruff check $(PKG_DIR)

mypy:
	@poetry run mypy $(PKG_DIR)

#------------------------#
#   FORMATTERS TARGETS   #
#------------------------#

.PHONY: formatting black

formatting: black ## Run all formatters

black:
	@poetry run black $(PKG_DIR) $(TEST_DIR)
