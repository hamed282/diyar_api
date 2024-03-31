from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel, ReserveModel, BenefitModel,\
    AboutModel, AboutPersonModel
from .serializers import BaseHomeSerializer, FeedbackSerializer, SocialMediaSerializer, PartnerLogoSerializer,\
    ReserveSerializer, BenefitSerializer, AboutSerializer, AboutPersonSerializer
from rest_framework import status


class HomeView(APIView):
    def get(self, request):
        base_home = BaseHomeModel.objects.all()
        ser_base_home = BaseHomeSerializer(instance=base_home, many=True)

        return Response(data={'home': ser_base_home.data})


class BenefitView(APIView):
    def get(self, request):
        benefit = BenefitModel.objects.all()
        ser_benefit = BenefitSerializer(instance=benefit, many=True)

        return Response(data=ser_benefit.data)


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


class ReserveView(APIView):
    """
    parameters:
    1. phone_number
    """
    def post(self, request):
        form = request.data
        ser_form = ReserveSerializer(data=form)
        if ser_form.is_valid():
            ser_form.save()
            return Response(data='registered!', status=status.HTTP_201_CREATED)
        else:
            return Response(data='invalid data', status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class AboutView(APIView):
    def get(self, request):
        about = AboutModel.objects.all()
        ser_about = AboutSerializer(instance=about, many=True)

        person = AboutPersonModel.objects.all()
        ser_person = AboutPersonSerializer(instance=person, many=True)

        return Response(data={'about': ser_about.data, 'person': ser_person.data})
