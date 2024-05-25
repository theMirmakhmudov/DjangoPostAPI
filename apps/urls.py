from django.urls import path
from .views import FaceCreateAPI, ExampleAPI

urlpatterns = [
    path("", FaceCreateAPI.as_view(), name="v1"),
    path("example", ExampleAPI.as_view(), name="v2")
]
