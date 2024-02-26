.PHONY: install-requirements
install-requirements:
	pip install -r requirements.txt

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: run-server
run-server:
	python manage.py runserver

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: update
update: install-requirements migrate ;

.PHONY: run-shell
run-shell:
	python manage.py shell