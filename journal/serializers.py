from rest_framework import serializers
from .models import JournalModel


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalModel
        fields = "__all__"
