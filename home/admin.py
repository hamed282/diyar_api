from django.contrib import admin
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel, ReserveModel, BenefitModel,\
    AboutModel, AboutPersonModel


class BenefitModelInline(admin.StackedInline):
    model = BenefitModel


class BaseHomeAdmin(admin.ModelAdmin):
    inlines = [BenefitModelInline]


admin.site.register(BaseHomeModel, BaseHomeAdmin)

# admin.site.register(BaseHomeModel)
admin.site.register(FeedbackModel)
admin.site.register(SocialMediaModel)
admin.site.register(PartnerLogoModel)


class ReserveAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'called']


admin.site.register(ReserveModel, ReserveAdmin)

# admin.site.register(BenefitModel)
admin.site.register(AboutModel)
admin.site.register(AboutPersonModel)
