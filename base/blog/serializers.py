from rest_framework import serializers
from .models import Ancient

class AncientSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)  # Assuming the 'id' field is read-only
    title = serializers.CharField(max_length=200)
    body = serializers.CharField(max_length=400)
    # created = serializers.DateTimeField()

    def create(self, validated_data):
        return Ancient.objects.create(**validated_data)
