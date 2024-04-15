from rest_framework import serializers
from .models import JournalModel


class JournalSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()

    class Meta:
        model = JournalModel
        fields = "__all__"

    def get_tag(self, obj):
        journal_name = obj
        journal = JournalModel.objects.get(product=journal_name)
        tags = journal.journal_tag.all()
        tag_list = [tag.tag.tag for tag in tags]
        return tag_list
