from rest_framework import routers
from .views import NoteViewSet

# Notes router
notes_router = routers.SimpleRouter()
notes_router.register(
    r'notes',
    NoteViewSet,
    basename='note',
)
