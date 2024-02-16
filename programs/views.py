from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProgramListModel
from .serializers import ProgramListSerializer


class ProgramListView(APIView):
    def get(self, request):
        program_list = ProgramListModel.objects.all()
        ser_list = ProgramListSerializer(instance=program_list, many=True)

        return Response(data=ser_list.data)
