from django.contrib import admin
from .models import JournalModel


class JournalAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(JournalModel, JournalAdmin)


