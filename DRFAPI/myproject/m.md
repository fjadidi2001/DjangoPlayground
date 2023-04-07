> create db with pg 

1. sudo -u postgres psql
2. create database dbname;
3. create user username with encrypted password 'password';
4. grant all privileges on database dbname to username;
>Setting up Django with dependencies

1. pip install -U django psycopg2-binary djangorestframework
2. python -m django startproject myproject .


>  Configuring database access in Django settings
 

1. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db-name>',
        'USER': '<db-user>',
        'PASSWORD': '<db-password>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```


2. python manage.py migrate

>Building a simple Django REST Framework API with PostgreSQL
1. python manage.py startapp notes
2. 
``` 
INSTALLED_APPS = [
    ... # Django apps are here
    'rest_framework',
    'notes.apps.NotesConfig',
]
```
<br>

3. Creating a simple model
``` 
from django.db import models

class Note(models.Model):
    text = models.TextField()
```


4. - python manage.py makemigrations
   - python manage.py migrate

5. Creating DRF serializers
``` 
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
```



<br>

**Serializers help convert data to and from JSON, but somehow we have to pass that data to them in the first place. This is where views come into play.**

<br>

