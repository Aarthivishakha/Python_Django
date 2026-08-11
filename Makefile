.PHONY: install migrate test build

install:
	pip install -r requirements.txt
	pip install -r quality/requirements.txt

migrate:
	python manage.py migrate --noinput

test:
	python manage.py test catalog

build:
	bash build.sh
