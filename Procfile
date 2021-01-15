release: python manage.py makemigration --noinput
release: python manage.py migrate --noinput
web: gunicorn portrapitstore.wsgi --log-file -
