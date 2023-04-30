from django.urls import path
from . import views
urlpatterns = [
    path('Gia', views.Gia),
    path('GoneGirl', views.Gone_Girl),
    path('<fuck>', views.dynamic_world),
]