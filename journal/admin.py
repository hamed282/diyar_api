from django.contrib import admin
from .models import JournalModel, AddTagModel


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class TagInline(admin.TabularInline):
    model = AddTagModel


class JournalAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]
    inlines = (TagInline,)


admin.site.register(JournalModel, JournalAdmin)
admin.site.register(AddTagModel, TagAdmin)
