from rest_framework import serializers
from .models import FaceModel


class FaceSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()
    image = serializers.ImageField()

    class Meta:
        model = FaceModel
        fields = ["id", "fullname", "user_id", "image"]

    def create(self, validated_data):
        return FaceModel.objects.create(**validated_data)
