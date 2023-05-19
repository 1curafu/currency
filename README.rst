'make run' - run the server
'make shell' - run the django shell
'make migrate' - run the migrations
'make makemigrations' - create new migrations
'make setup' - run the setup script
'make createsuperuser' - create a superuser
'brew services start/stop rabbitmq' - start/stop rabbitmq
'python app/manage.py test_data' - create test data
'gunicorn --workers 4 --threads 4 settings.wsgi --timeout 30 --max-requests 10000 --log-level info --bind 0.0.0.0:8000' - gunicorn start command