from django.contrib import admin
from .models import CategoryProgramModel, SubCategoryProgramModel


# class ProgramModelAdmin(admin.ModelAdmin):
#     readonly_fields = ["slug"]


# class ProgramModelInline(admin.StackedInline):
#     model = ProgramModel
#     readonly_fields = ["slug"]
#     # exclude = ("e",)  # optional
#     # list_display = ('pk', 'name')
#     # readonly_fields = ('id',)
#     # can_delete = False
#     # classes = ['collapse']
#     # verbose_name_plural = 'Translation Files'


# class ProgramModelAdmin(admin.ModelAdmin):
#     inlines = [ProgramModelInline]


# admin.site.register(ProgramDescriptionModel, ProgramModelAdmin)

class CategoryProgramAdmin(admin.ModelAdmin):
    list_display = ['category']
    readonly_fields = ['slug']


class SubCategoryProgramAdmin(admin.ModelAdmin):
    list_display = ['subcategory']
    readonly_fields = ['slug']


admin.site.register(CategoryProgramModel, CategoryProgramAdmin)
admin.site.register(SubCategoryProgramModel, SubCategoryProgramAdmin)

