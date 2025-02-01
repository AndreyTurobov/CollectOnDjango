PYTHON = python
MANAGE = $(PYTHON) manage.py
RUFF = ruff

.PHONY: run make-m migrate su test lint format fake

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

fake:
	${MANAGE} fake_db --count 20