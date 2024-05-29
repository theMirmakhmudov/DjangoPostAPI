from django.urls import path
from .views import FaceCreateAPI, CheckFaceCreateAPI

urlpatterns = [
    path("", FaceCreateAPI.as_view(), name="v1"),
    path("v2", CheckFaceCreateAPI.as_view(), name="v2")
]
