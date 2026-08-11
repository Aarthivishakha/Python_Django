.PHONY: install migrate test tools tools-project build

install:
	pip install -r requirements.txt
	pip install -r Python_3.9/requirements.txt

migrate:
	python manage.py migrate --noinput

test:
	python manage.py test

tools:
	bash Python_3.9/run_all.sh

tools-project:
	bash Python_3.9/run_on_project.sh

build:
	bash build.sh
