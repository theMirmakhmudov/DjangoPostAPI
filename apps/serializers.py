from rest_framework import serializers
from .models import FaceModel, ExampleModel


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceModel
        fields = ("id", "fullname", "user_id", "image")


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ("id", "fullname", "user_id")
