from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel
from .serializers import BaseHomeSerializer, FeedbackSerializer, SocialMediaSerializer, PartnerLogoSerializer


class HomeView(APIView):
    def get(self, request):
        base_home = BaseHomeModel.objects.all()
        ser_base_home = BaseHomeSerializer(instance=base_home, many=True)

        return Response(data={'home': ser_base_home.data})


class FeedbackView(APIView):
    def get(self, request):
        feedback = FeedbackModel.objects.all()
        ser_feedback = FeedbackSerializer(instance=feedback, many=True)

        return Response(data={'feedback': ser_feedback.data})


class SocialMediaView(APIView):
    def get(self, request):
        social_media = SocialMediaModel.objects.all()
        ser_social_media = SocialMediaSerializer(instance=social_media, many=True)

        return Response(data={'social_media': ser_social_media.data})


class PartnerLogoView(APIView):
    def get(self, request):
        partner_logo = PartnerLogoModel.objects.all()
        ser_partner_logo = PartnerLogoSerializer(instance=partner_logo, many=True)

        return Response(data={'partner_logo': ser_partner_logo.data})
