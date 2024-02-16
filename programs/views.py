from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProgramListModel, ProgramModel
from .serializers import ProgramListSerializer, ProgramSerializer
from django.shortcuts import get_object_or_404


class ProgramListView(APIView):
    def get(self, request):
        program_list = ProgramListModel.objects.all()
        ser_list = ProgramListSerializer(instance=program_list, many=True)

        return Response(data=ser_list.data)


class ProgramView(APIView):
    """
    get parameter:
    1. program_slug
    """
    def get(self, request):
        program_slug = self.request.query_params.get('program_slug')

        program = get_object_or_404(ProgramListModel, slug=program_slug)
        program = program.slug_program.all()

        ser_program = ProgramSerializer(instance=program, many=True)
        return Response(data=ser_program.data)
