from rest_framework import routers
from django.urls import path, include

from .views import NoteViewSet

notes_router = routers.SimpleRouter()
notes_router.register(
    r'notes',
    NoteViewSet,
    basename='note',
)
urlpatterns = [

    path('notes/', include(notes_router.urls))
]