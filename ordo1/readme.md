# django-admin
### manage.py
This file should not be modified; it manages the project and allows us to run it.
### __init__.py
This file enables module creation.
### asgi.py & wsgi.py
Used for deploying the project.
### settings.py
Houses global settings.
### urls.py
Manipulating this file controls which files are visible to users.
# startapp
### migration and models.py
These return changes to the database. Migrations save database modifications, while models save entities.
### admin.py
Configures and displays items in models. 
### tests.py
Used for writing tests.
### views.py
Determines what to display to the user.<br>
*When creating an app, remember to add it to INSTALLED_APPS in settings.*
# url
URLs are responsible for site addressing.
# view
Contains functions and classes for handling URLs.<br>
Returns results based on HttpResponse and utilizes URLs for execution.
