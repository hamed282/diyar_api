from rest_framework import serializers
from .models import ProgramModel, ProgramDescriptionModel


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramModel
        fields = ['title', 'description', 'content', 'slug']
        depth = 1


class ProgramListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramModel
        fields = ['icon', 'title_link', 'slug']
