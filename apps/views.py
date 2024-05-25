from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import FaceSerializer, ExampleSerializer
from .models import FaceModel, ExampleModel


class FaceCreateAPI(ListCreateAPIView):
    queryset = FaceModel.objects.all()
    serializer_class = FaceSerializer

class ExampleAPI(ListCreateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer
