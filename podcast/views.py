from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PodcastModel
from .serializers import PodcastSerializer


class PodcastView(APIView):
    def get(self, request):
        podcast = PodcastModel.objects.all()
        ser_podcast = PodcastSerializer(instance=podcast, many=True)
        return Response(data=ser_podcast.data)
