
from django.urls import path
from .views import NoteViewSet

urlpatterns = [
    path('Note/', NoteViewSet.as_view()),
]