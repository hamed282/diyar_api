from django.contrib import admin
from .models import ProgramModel, ProgramDescriptionModel


class ProgramModelAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(ProgramModel, ProgramModelAdmin)
admin.site.register(ProgramDescriptionModel)
