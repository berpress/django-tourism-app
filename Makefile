lint:
	@pre-commit run --all-files

start:
	@python manage.py runserver
