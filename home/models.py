from django.db import models
from accounts.models import User


class SuccessVisaModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_success')


class FixRejectionModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_fix_reject')


class BaseHomeModel(models.Model):
    success_visa = models.IntegerField()
    fix_rejection = models.IntegerField()
    founder_image = models.ImageField(upload_to='images/home/')
    founder_video = models.FileField(upload_to='videos/home/')
    content_bottom = models.TextField(max_length=10000)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)


class PartnerLogoModel(models.Model):
    name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='images/partner_logo/')


class FeedbackModel(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/feedback/')
    city = models.CharField(max_length=64)
    rank = models.IntegerField()
    content = models.TextField(max_length=1024)


class SocialMediaModel(models.Model):
    name = models.CharField(max_length=32)
    logo = models.ImageField(upload_to='images/social_media/')
    address = models.CharField(max_length=200)
    priority = models.IntegerField()
