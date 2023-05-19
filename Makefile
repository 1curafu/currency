
manage_py := docker compose exec -it backend python app/manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

collectstatic:
	$(manage_py) collectstatic --no-input && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

setup:
	pip install -r requirements.txt

createsuperuser:
	$(manage_py) createsuperuser

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	docker compose exec -it backend pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=79.7754

docker:
	docker-compose up -d --build

gunicorn:
	cd app && gunicorn --workers 4 settings.wsgi --max-requests 10000 --log-level info --bind 0.0.0.0:8000