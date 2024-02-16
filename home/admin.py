from django.contrib import admin
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel, ReserveModel, BenefitModel,\
    AboutModel, AboutPersonModel


admin.site.register(BaseHomeModel)
admin.site.register(FeedbackModel)
admin.site.register(SocialMediaModel)
admin.site.register(PartnerLogoModel)


class ReserveAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'called']


admin.site.register(ReserveModel, ReserveAdmin)

admin.site.register(BenefitModel)
admin.site.register(AboutModel)
admin.site.register(AboutPersonModel)
