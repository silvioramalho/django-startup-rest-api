# Django API - Startup Project
# DJOSER + DJANGO REST FRAMEWORK JWT

## requirements

```
astroid==2.3.2
Django==2.2.7
django-cors-headers==3.2.0
django-debug-toolbar==2.1
django-otp==0.7.3
django-request-logging==0.7.0
django-templated-mail==1.1.1
djangorestframework==3.10.3
djangorestframework-jwt==1.11.0
djangorestframework-simplejwt==4.3.0
djoser==2.0.3
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
Pillow==6.2.1
PyJWT==1.7.1
pylint==2.4.3
python-decouple==3.3
pytz==2019.3
six==1.12.0
sqlparse==0.3.0
typed-ast==1.4.0
wrapt==1.11.2
```

## Development Install

### Clone Repo

```
git clone git@github.com:silvioramalho/django-boilerplate-api.git <backend-name>

cd <backend-name>

python3 -m venv env
. env/bin/activate

pip install --upgrade pip
pip install -r requirements-dev.txt

cd BackendAPI
python manage.py collectstatic

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

`Nota: Caso seja alterado algum item do template, é necessário retirar do .gitignore a pasta static`


## Creating .env file

Create a .env file at the root path and insert the following variables


```
SECRET_KEY=xxxxyyyyttttttxxxxyyyyyyxxxxxxxoooooiiii
DEBUG=True

FRONTEND_URL=localhost:4200

EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=google-app-password
EMAIL_PORT=587
EMAIL_USE_TLS =True
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

`Note: Without spaces and single quotes`