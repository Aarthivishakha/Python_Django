.PHONY: install migrate test tools tools-project build

install:
	pip install -r requirements.txt
	pip install -r tools/requirements.txt

migrate:
	python manage.py migrate --noinput

test:
	python manage.py test

tools:
	bash tools/run_all.sh

tools-project:
	bash tools/run_on_project.sh

build:
	bash build.sh
