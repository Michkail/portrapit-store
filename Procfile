release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
web: gunicorn portrapitstore.wsgi --log-file -
