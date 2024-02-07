from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AnswerRecommenderModel
from .serializers import AnswerRecommenderSerializer


class RecommenderResultView(APIView):
    def post(self, request):
        form = request.data
        ser_form = AnswerRecommenderSerializer(data=form)
        if ser_form.is_valid():
            ser_form.save()
            # AnswerRecommenderModel.objects.create()
        return Response(data='hi')
