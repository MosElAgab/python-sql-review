#################################################################################
#
# Makefile to build the project
#
#################################################################################

# 
PROJECT_NAME = python-sql-review
REGION = eu-west-2
PYTHON_INTERPRETER = python
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip

# 
## Create python interpreter environment (venv).
create-environment:
	@echo ">>> About to create environment: $(PROJECT_NAME)..."
	@echo ">>> check python3 version"
	( \
		$(PYTHON_INTERPRETER) --version; \
	)
	@echo ">>> Setting up VirtualEnv."
	( \
	    $(PIP) install -q virtualenv virtualenvwrapper; \
	    virtualenv venv --python=$(PYTHON_INTERPRETER); \
	)

# Define utility variable to help calling Python from the virtual environment
ACTIVATE_ENV := source venv/bin/activate

# Execute python related functionalities from within the project's environment
define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

## print requirement
print-req:
	$(call execute_in_env, ${PIP} freeze > requirements.txt)

## Install flake8
flake:
	$(call execute_in_env, $(PIP) install flake8)

## Install pytest
pytest:
	$(call execute_in_env, $(PIP) install pytest)


## setup database
setup-database:
	$(call execute_in_env, psql -f db/setup-db.sql)

# Run the flake8 code check
run-flake:
	$(call execute_in_env, flake8 \
	./src/utilities.py \
	./test/test_format_departments.py \
	./test/test_format_stock.py \
	./test/test_format_staff.py \
	./test/test_format_stock_feature.py )	

## Run a single test
test-this:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v ${test_run})

## Run all the unit tests
test-all:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v)

## Run all checks
run-checks: test-all run-flake 

## install pg8000
pg8000:
	$(call execute_in_env, $(PIP) install pg8000)