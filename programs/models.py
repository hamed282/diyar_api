from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class ProgramListModel(models.Model):
    program = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='images/programs/')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.slug}'


class ProgramModel(models.Model):
    title = models.CharField(max_length=100)
    content_up = CKEditor5Field(config_name='extends')
    content_bottom = CKEditor5Field(config_name='extends')
    slug = models.ForeignKey(ProgramListModel, on_delete=models.CASCADE, related_name='slug_program')

    def __str__(self):
        return f'{self.slug}'
