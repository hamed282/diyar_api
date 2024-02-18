from rest_framework.views import APIView
from .models import JournalModel
from . serializers import JournalSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class JournalListView(APIView):
    def get(self, request):
        """
        get parameter:
        1. limit
        """
        journal_limit = self.request.query_params.get('limit', None)
        # journal_sort = self.request.query_params.get('sort')

        if journal_limit is None:
            journal = JournalModel.objects.all().order_by('-created')
        else:
            journal = JournalModel.objects.all().order_by('-created')[:int(journal_limit)]
        # journal = journal.order_by('created')
        ser_journal = JournalSerializer(instance=journal, many=True)

        return Response(data=ser_journal.data)


class JournalView(APIView):
    def get(self, request):
        """
        get parameter:
        1. journal_slug
        """
        journal_slug = self.request.query_params.get('journal_slug')

        journal = get_object_or_404(JournalModel, slug=journal_slug)
        ser_journal = JournalSerializer(instance=journal)

        return Response(data=ser_journal.data)
