from rest_framework import serializers
from .models import ProgramListModel, ProgramModel


class ProgramListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramListModel
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    slug = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = ProgramModel
        fields = '__all__'
