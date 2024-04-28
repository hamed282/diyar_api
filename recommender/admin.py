from django.contrib import admin
from .models import (PersonalInformationModel, SkillModel, IncomeModel, EducationalRecordModel, JobRecordModel,
                     QuestionModel, AddAnswerModel, AnswerModel)


class AnswerInline(admin.TabularInline):
    model = AddAnswerModel
    # raw_id_fields = ('product',)
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']
    inlines = (AnswerInline,)


admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(AnswerModel)
admin.site.register(PersonalInformationModel)
admin.site.register(IncomeModel)
admin.site.register(JobRecordModel)
admin.site.register(SkillModel)
admin.site.register(EducationalRecordModel)


