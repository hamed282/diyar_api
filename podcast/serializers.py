from rest_framework import serializers
from .models import PodcastModel


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastModel
        fields = '__all__'
