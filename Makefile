PYTHON = python
MANAGE = $(PYTHON) manage.py
RUFF = ruff

.PHONY: run make-m migrate su test lint format

run:
	${MANAGE} runserver

make-m:
	${MANAGE} makemigrations

migrate:
	${MANAGE} migrate

test:
	${MANAGE} test

su:
	${MANAGE} createsuperuser

lint:
	${RUFF} check .

format:
	${RUFF} --fix .