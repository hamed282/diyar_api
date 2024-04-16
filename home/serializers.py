from rest_framework import serializers
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel, ReserveModel, BenefitModel,\
    AboutModel, AboutPersonModel


class BaseHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseHomeModel
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = '__all__'


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitModel
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
        fields = ['phone_number']


class AboutPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPersonModel
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutModel
        fields = '__all__'
