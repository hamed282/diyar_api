from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProgramModel
from .serializers import ProgramSerializer, ProgramListSerializer
from django.shortcuts import get_object_or_404


class ProgramListView(APIView):
    def get(self, request):
        program_list = ProgramModel.objects.all()
        ser_list = ProgramListSerializer(instance=program_list, many=True)

        return Response(data=ser_list.data)


class ProgramView(APIView):
    def get(self, request):
        """
        get parameter:
        1. program_slug
        """
        program_slug = self.request.query_params.get('program_slug')

        program = get_object_or_404(ProgramModel, slug=program_slug)
        ser_program = ProgramSerializer(instance=program)

        return Response(data=ser_program.data)
