from django.contrib import admin
from .models import ProgramModel, ProgramDescriptionModel


# class ProgramModelAdmin(admin.ModelAdmin):
#     readonly_fields = ["slug"]


class ProgramModelInline(admin.StackedInline):
    model = ProgramModel
    readonly_fields = ["slug"]
    # exclude = ("e",)  # optional
    # list_display = ('pk', 'name')
    # readonly_fields = ('id',)
    # can_delete = False
    # classes = ['collapse']
    # verbose_name_plural = 'Translation Files'


class ProgramModelAdmin(admin.ModelAdmin):
    inlines = [ProgramModelInline]


admin.site.register(ProgramDescriptionModel, ProgramModelAdmin)

# admin.site.register(ProgramModel, ProgramModelAdmin)
# admin.site.register(ProgramDescriptionModel)
