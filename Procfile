release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py createsuperuser
web: gunicorn portrapitstore.wsgi --log-file -
