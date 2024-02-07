from django.contrib import admin
from .models import BaseHomeModel, FeedbackModel, SocialMediaModel, PartnerLogoModel


admin.site.register(BaseHomeModel)
admin.site.register(FeedbackModel)
admin.site.register(SocialMediaModel)
admin.site.register(PartnerLogoModel)

