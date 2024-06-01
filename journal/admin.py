from django.contrib import admin
from .models import JournalModel, AddTagModel, TagModel


class TagAdmin(admin.ModelAdmin):
    # readonly_fields = ["slug"]
    list_display = ['tag']


class TagInline(admin.TabularInline):
    model = AddTagModel


class JournalAdmin(admin.ModelAdmin):
    # readonly_fields = ["slug"]
    inlines = (TagInline,)


admin.site.register(JournalModel, JournalAdmin)
admin.site.register(TagModel, TagAdmin)
