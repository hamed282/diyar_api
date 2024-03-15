from django.contrib import admin
from .models import PodcastModel


class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'created']
    readonly_fields = ["slug"]


admin.site.register(PodcastModel, PodcastAdmin)
