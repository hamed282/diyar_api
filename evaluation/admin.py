from django.contrib import admin
from .models import ChildrenAgeModel, EvaluationModel, EducationModel, PartnerEducationModel,\
    PartnerWorkExperiencesModel, WorkExperiencesModel


class ChildrenAgeInline(admin.StackedInline):
    model = ChildrenAgeModel
    extra = 1


class EducationInline(admin.StackedInline):
    model = EducationModel
    extra = 1


class PartnerEducationInline(admin.StackedInline):
    model = PartnerEducationModel
    extra = 1


class PartnerWorkExperiencesInline(admin.StackedInline):
    model = PartnerWorkExperiencesModel
    extra = 1


class WorkExperiencesInline(admin.StackedInline):
    model = WorkExperiencesModel
    extra = 1


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    inlines = [ChildrenAgeInline, EducationInline, WorkExperiencesInline, PartnerEducationInline,
               PartnerWorkExperiencesInline]
# class EvaluationAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name']


admin.site.register(EvaluationModel, EvaluationAdmin)

