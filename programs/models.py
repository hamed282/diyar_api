from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class ProgramModel(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/programs/icon/')
    content_up = CKEditor5Field(config_name='extends')
    content_bottom = CKEditor5Field(config_name='extends')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.slug}'
