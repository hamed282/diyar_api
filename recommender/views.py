from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (QuestionModel, SkillModel, IncomeModel, PersonalInformationModel, JobRecordModel,
                     EducationalRecordModel)
from .serializers import (PersonalInformationSerializer, SkillSerializer, IncomeSerializer, JobRecordSerializer,
                          EducationalRecordSerializer)


class PersonalInformationView(APIView):
    def get(self, request):
        personal_information = PersonalInformationModel.objects.all()
        ser_data = PersonalInformationSerializer(instance=personal_information, many=True)

        return Response(data=ser_data.data)


class JobRecordView(APIView):
    def get(self, request):
        personal_information = JobRecordModel.objects.all()
        ser_data = JobRecordSerializer(instance=personal_information, many=True)

        return Response(data=ser_data.data)


class EducationalRecordView(APIView):
    def get(self, request):
        personal_information = EducationalRecordModel.objects.all()
        ser_data = EducationalRecordSerializer(instance=personal_information, many=True)

        return Response(data=ser_data.data)


class IncomeView(APIView):
    def get(self, request):
        personal_information = IncomeModel.objects.all()
        ser_data = IncomeSerializer(instance=personal_information, many=True)

        return Response(data=ser_data.data)


class SkillView(APIView):
    def get(self, request):
        personal_information = SkillModel.objects.all()
        ser_data = SkillSerializer(instance=personal_information, many=True)

        return Response(data=ser_data.data)


class RecommenderView(APIView):
    def post(self, request):
        return Response(data='data')

