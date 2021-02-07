from rest_framework import serializers

from .models import Docx

class FileSerializer(serializers.ModelSerializer):
    """Сериализация файла"""
    class Meta:
        model = Docx
        fields = {'file'}

