from rest_framework import serializers
from .models import JournalModel


class JournalSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()

    class Meta:
        model = JournalModel
        fields = "__all__"

    def get_tag(self, obj):
        # product_name = obj
        # product = ProductModel.objects.get(product=product_name)
        # subcategories = product.subcategory_product.all()
        # subcategory_list = [subcategory.subcategory.subcategory for subcategory in subcategories]
        return 'tag'
