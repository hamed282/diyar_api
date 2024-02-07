from rest_framework import serializers
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel, ReserveModel


class BaseHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseHomeModel
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaModel
        fields = '__all__'


class PartnerLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerLogoModel
        fields = '__all__'


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveModel
        fields = '__all__'
