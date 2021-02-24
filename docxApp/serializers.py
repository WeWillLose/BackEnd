from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    """Сериализация файла"""
    class Meta:
        fields = {'file'}

