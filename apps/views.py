from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import FaceSerializer, CheckFaceSerializer
from .models import FaceModel, CheckFaceModel


class FaceCreateAPI(ListCreateAPIView):
    queryset = FaceModel.objects.all()
    serializer_class = FaceSerializer


class CheckFaceCreateAPI(ListCreateAPIView):
    queryset = CheckFaceModel.objects.all()
    serializer_class = CheckFaceSerializer
