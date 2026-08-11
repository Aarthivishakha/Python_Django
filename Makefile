.PHONY: install syncdb test build

install:
	pip install -r requirements.txt

syncdb:
	python manage.py syncdb --noinput

test:
	python manage.py test catalog

build:
	bash build.sh
