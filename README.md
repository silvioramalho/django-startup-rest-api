# Django API - Startup Project

Using DJOSER + DJANGO REST FRAMEWORK JWT

I decided to create this boilerplate to facilitate the implementation of new solutions, where in most cases it is necessary to provide the features that this project has.


## Features

- REST API with JWT
- Send activation email on register (REST API)
- Login with email
- Activate multiple users
- Send confirmation email
- Block user
- Resend activation email
- Send link to change password (Frontend necessary)
- Application that fix a `rest_framework_jwt` issue


## Development Install

### Clone Repo

```
git clone git@github.com:silvioramalho/django-boilerplate-api.git <your-backend-name>
```

### Setup env

```
cd <your-backend-name>
python3 -m venv env
. env/bin/activate
```

### Upgrade pip

```
pip install --upgrade pip
```

### Install Dependencies (dev)

```
pip install -r requirements-dev.txt
```
### Creating .env file

Create an .env file at the root path and insert the following variables

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

### Collects the static files

```
cd BackendAPI
python manage.py collectstatic
```

###  Apply migrations
```
python manage.py migrate
```

### Create super user
```
python manage.py createsuperuser
```

### Run server
```
python manage.py runserver
```

### Access

> http://127.0.0.1:8000/admin/

`Note: If any item in the template is changed, it will be necessary to remove the static folder from .gitignore file`


