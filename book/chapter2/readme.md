1. django-admin startproject name
2. python3 manage.py migrate
3. python3 manage.py startapp another-name
4. change settings.py(in project)
add this to INSTALLED_APPS:
"another-name.apps.Another-nameConfig"
5. added this to apps.py in app file

    ```
    from django.apps import AppConfig


    class Another-nameConifg(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'another-name'

    ```


 
6. added sth you want see on your website to views.py in the app

    ``` 
    from django.http import HttpResponse
    def homePageView(request):
        return HttpResponse("Hello, World!")
    ```

7. make urls.py in app directory 
and added this:
    ``` 
    from django.urls import path
    from .views import homePageView
    urlpatterns = [
        path("", homePageView, name="home"),
    ]
    ```
8. added this to urls.py in main dir
``` 
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("another-name.urls")),
]
```
9. python3 manage.py runserver