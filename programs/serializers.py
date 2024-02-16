from rest_framework import serializers
from .models import ProgramListModel


class ProgramListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramListModel
        fields = '__all__'
