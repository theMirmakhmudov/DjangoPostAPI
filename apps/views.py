from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import FaceSerializer
from .models import FaceModel


class FaceCreateAPI(CreateAPIView):
    queryset = FaceModel.objects.all()
    serializer_class = FaceSerializer


class FaceListAPI(ListAPIView):
    queryset = FaceModel.objects.all()
    serializer_class = FaceSerializer
