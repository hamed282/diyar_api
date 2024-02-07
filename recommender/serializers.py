from rest_framework import serializers
from .models import AnswerRecommenderModel


class AnswerRecommenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerRecommenderModel
        fields = '__all__'

