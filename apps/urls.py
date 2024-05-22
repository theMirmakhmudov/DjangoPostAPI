from django.urls import path
from .views import FaceCreateAPI, FaceListAPI

urlpatterns = [
    path("create", FaceCreateAPI.as_view(), name="create"),
    path("", FaceListAPI.as_view(), name="listview"),
]
