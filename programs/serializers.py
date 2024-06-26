from rest_framework import serializers
from .models import CategoryProgramModel, SubCategoryProgramModel


# class ProgramSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ProgramModel
#         fields = ['title', 'description', 'content', 'slug']
#         depth = 1
#
#
# class ProgramListSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ProgramModel
#         fields = ['icon', 'title_link', 'slug']


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProgramModel
        fields = ['category', 'icon', 'slug']


class SubCategoryListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)

    class Meta:
        model = SubCategoryProgramModel
        fields = ['category', 'subcategory', 'media', 'title', 'slug']


class CategoryProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProgramModel
        # fields = ['category', 'banner', 'icon', 'title', 'description', 'slug']
        fields = '__all__'


class SubCategoryProgramSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)

    class Meta:
        model = SubCategoryProgramModel
        # fields = ['category', 'subcategory', 'banner', 'title', 'content', 'description', 'slug']
        fields = '__all__'
