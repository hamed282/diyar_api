from django.contrib import admin
from .models import PodcastModel


class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'created']


admin.site.register(PodcastModel, PodcastAdmin)
