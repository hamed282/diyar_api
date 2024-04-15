from rest_framework import serializers
from .models import JournalModel


class JournalSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()

    class Meta:
        model = JournalModel
        fields = "__all__"

    def get_tag(self, obj):
        title_journal = obj
        print(type(title_journal))
        # journal = JournalModel.objects.get(title=title_journal)
        # tags = journal.journal_tag.all()
        # tag_list = [tag.tag.tag for tag in tags]
        return 'tag_list'
