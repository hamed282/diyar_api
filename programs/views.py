from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SubCategoryProgramModel, CategoryProgramModel
from .serializers import (CategoryListSerializer, SubCategoryListSerializer, CategoryProgramSerializer,
                          SubCategoryProgramSerializer)
from django.shortcuts import get_object_or_404


# class ProgramListView(APIView):
#     def get(self, request):
#         program_list = ProgramModel.objects.all()
#         ser_list = ProgramListSerializer(instance=program_list, many=True)
#
#         return Response(data=ser_list.data)


# class ProgramView(APIView):
#     def get(self, request):
#         """
#         get parameter:
#         1. program_slug
#         """
#         program_slug = self.request.query_params.get('program_slug')
#
#         program = get_object_or_404(ProgramModel, slug=program_slug)
#         ser_program = ProgramSerializer(instance=program)
#
#         return Response(data=ser_program.data)


class CategoryListView(APIView):
    def get(self, request):
        category_list = CategoryProgramModel.objects.all()
        ser_data = CategoryListSerializer(instance=category_list, many=True)

        return Response(data=ser_data.data)


class SubCategoryListView(APIView):
    def get(self, request):
        subcategory_list = SubCategoryProgramModel.objects.all()
        ser_data = SubCategoryListSerializer(instance=subcategory_list, many=True)

        return Response(data=ser_data.data)


class CategoryProgramView(APIView):
    def get(self, request):
        """
            get parameter:
            1. category_slug
        """
        category_slug = self.request.query_params.get('category_slug')

        category = get_object_or_404(CategoryProgramModel, slug=category_slug)
        ser_data = CategoryProgramSerializer(instance=category)

        return Response(data=ser_data.data)


class SubCategoryProgramView(APIView):
    def get(self, request):
        """
            get parameter:
            1. subcategory_slug
        """
        subcategory_slug = self.request.query_params.get('subcategory_slug')

        subcategory = get_object_or_404(SubCategoryProgramModel, slug=subcategory_slug)
        ser_data = SubCategoryProgramSerializer(instance=subcategory)

        return Response(data=ser_data.data)
