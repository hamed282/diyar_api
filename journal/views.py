from django.shortcuts import render
from rest_framework.views import APIView
from .models import JournalModel
from . serializers import JournalSerializer
from rest_framework.response import Response


class JournalView(APIView):
    def get(self, request):
        journal = JournalModel.objects.all()
        ser_journal = JournalSerializer(instance=journal, many=True)

        return Response(data=ser_journal.data)


class JournalShowView(APIView):
    def get(self, request):
        """
        get parameter:
        1. journal_id
        """
        journal_id = self.request.query_params.get('journal_id')

        journal = JournalModel.objects.get(pk=journal_id)
        ser_journal = JournalSerializer(instance=journal)

        return Response(data=ser_journal.data)
