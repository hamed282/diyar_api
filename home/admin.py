from django.contrib import admin
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel, ReserveModel, BenefitModel,\
    AboutModel, AboutPersonModel, SuccessVisaModel, FixRejectionModel


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name']
    # readonly_fields = ['name', 'image', 'city', 'rate', 'content']


class ReserveAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'called']
    readonly_fields = ['phone_number']


class BenefitModelInline(admin.StackedInline):
    model = BenefitModel


class SuccessVisaModelInline(admin.StackedInline):
    model = SuccessVisaModel


class FixRejectionModelInline(admin.StackedInline):
    model = FixRejectionModel


class PartnerLogoModelInline(admin.StackedInline):
    model = PartnerLogoModel


class SocialMediaModelInline(admin.StackedInline):
    model = SocialMediaModel


class BaseHomeAdmin(admin.ModelAdmin):
    inlines = [BenefitModelInline]


admin.site.register(BaseHomeModel, BaseHomeAdmin)
admin.site.register(FeedbackModel, FeedbackAdmin)
# admin.site.register(SocialMediaModel)
# admin.site.register(PartnerLogoModel)
admin.site.register(ReserveModel, ReserveAdmin)

# admin.site.register(BenefitModel)
admin.site.register(AboutModel)
admin.site.register(AboutPersonModel)
