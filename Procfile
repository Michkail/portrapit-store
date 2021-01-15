release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn portrapitstore.wsgi --log-file -
