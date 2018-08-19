.PHONY: build
build: setup-django seed-db
	pip install -r requirements.txt

.PHONY: setup-django
setup-django:
	python manage.py makemigrations
	python manage.py migrate

.PHONY: seed-db
seed-db:
	python manage.py loaddata ./fixtures/candidates.json
	python manage.py loaddata ./fixtures/queries.json

.PHONY: server
server: build
	python manage.py runserver

.PHONY: celery
celery:
	celery -A elections worker -B --concurrency=1 -l INFO
