from django.db import models
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field


class SuccessVisaModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_success')


class FixRejectionModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_fix_reject')


class BenefitModel(models.Model):
    base_home = models.OneToOneField('BaseHomeModel', on_delete=models.CASCADE)
    row = models.TextField()

    def __str__(self):
        return self.row


class BaseHomeModel(models.Model):
    user_count = models.IntegerField()
    success_visa = models.IntegerField()
    fix_rejection = models.IntegerField()
    founder_image = models.ImageField(upload_to='images/home/')
    founder_video = models.FileField(upload_to='videos/home/')
    content_bottom = CKEditor5Field(config_name='extends')
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'


class PartnerLogoModel(models.Model):
    name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='images/partner_logo/')

    class Meta:
        verbose_name = 'Partner Logo'
        verbose_name_plural = 'Partner Logo'


class FeedbackModel(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/feedback/')
    city = models.CharField(max_length=64)
    rate = models.IntegerField()
    content = models.TextField(max_length=1024)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'


class SocialMediaModel(models.Model):
    name = models.CharField(max_length=32)
    logo = models.ImageField(upload_to='images/social_media/')
    address = models.CharField(max_length=200)
    priority = models.IntegerField()

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'


class ReserveModel(models.Model):
    phone_number = models.CharField(max_length=30)
    called = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.phone_number}'

    class Meta:
        verbose_name = 'Reserve'
        verbose_name_plural = 'Reserves'


class AboutPersonModel(models.Model):
    image = models.ImageField(upload_to='images/about/person/')
    full_name = models.CharField(max_length=100)
    job = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'About Person'
        verbose_name_plural = 'About Person'


class AboutModel(models.Model):
    image = models.ImageField(upload_to='images/about/')
    content = CKEditor5Field(config_name='extends')
    video = models.FileField(upload_to='videos/about/')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
