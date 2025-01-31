PYTHON = python
MANAGE = $(PYTHON) manage.py


.PHONY: run makemigrations migrate su test

run:
	${MANAGE} runserver
make:
	${MANAGE} makemigrations
migrate:
	${MANAGE} migrate
test:
	${MANAGE} test
su:
	${MANAGE} createsuperuser