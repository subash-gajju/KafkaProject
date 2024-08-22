from rest_framework import generics
from .models import FaceEmbed
from .serializers import FaceEmbedSerializer

class FaceEmbedList(generics.ListAPIView):
    queryset = FaceEmbed.objects.all()
    serializer_class = FaceEmbedSerializer