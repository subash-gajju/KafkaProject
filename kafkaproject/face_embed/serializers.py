from rest_framework import serializers
from .models import FaceEmbed

class FaceEmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceEmbed
        fields = '__all__'
