from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home),
    path('about', views.About),
    path('contact', views.contact),
    path('link', views.link),
]
