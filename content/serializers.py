from rest_framework import serializers
from .models import Contents


class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['name']
