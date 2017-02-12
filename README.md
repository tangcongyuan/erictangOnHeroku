# DjangoRestFrameworkOnAWS
## Documentation is a virtue.

## Installing Django and Django Rest Framework
```
pip install django djangorestframework djangorestframework-jwt
```

## Creating website and apps
```
django-admin startproject tangcongyuan
python manage.py startapp main
python manage.py startapp authentication
```

## After setting up our authentication Account
```
python manage.py makemigrations
python manage.py migrate
```

## Don't forget to create a superuser
```
python manage.py createsuperuser
```

## In order to update Account last_login field when a user login with JWT, we need to overwrite this file: *.../env/Lib/site-packages/rest_framework_jwt/views.py*

```python
...
# Added for updating last_login
from django.utils import timezone
...
def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if serializer.is_valid():
        user = serializer.object.get('user') or request.user

        # Added for updating last_login
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        token = serializer.object.get('token')
        response_data = jwt_response_payload_handler(token, user, request)

        return Response(response_data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
...
```

## How to dump data that we already have?
### Just to save ourselves some trouble creating all the Accounts for Authentication
```
python manage.py dumpdata authentication --indent=4 > seed.json
```
Then move the created json file into `/authentication/fixtures/` folder. That's where our data will be loaded using:
```
python manage.py loaddata seed.json
```
And, for your reference, here's how to remove all existing data in the database:
```
python manage.py flush
```

## Deploy to Heroku
### You have to clone from Heroku's sample repo
### Useful commands:
```
heroku create app-name
git push heroku master
heroku ps:scale web=1
heroku open
```
