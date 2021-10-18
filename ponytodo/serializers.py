from rest_framework import serializers
from .models import Ponytodo

class PonytodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponytodo
        fields = ('id', 'title', 'description', 'completed')