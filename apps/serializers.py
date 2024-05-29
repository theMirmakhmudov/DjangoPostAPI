from rest_framework import serializers
from .models import FaceModel, CheckFaceModel


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceModel
        fields = ("id", "fullname", "user_id", "image")


class CheckFaceSerializer(serializers.ModelSerializer):
    FaceModelCheck = FaceSerializer()

    class Meta:
        model = CheckFaceModel
        fields = ('id', 'FaceModelCheck')
