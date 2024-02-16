from rest_framework import serializers
from .models import ProgramModel


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramModel
        fields = '__all__'


class ProgramListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramModel
        fields = ['icon', 'title', 'slug']
