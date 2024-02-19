from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class ProgramDescriptionModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'


class ProgramModel(models.Model):
    title_link = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/programs/icon/')

    title = models.CharField(max_length=100)
    description = models.ForeignKey(ProgramDescriptionModel, on_delete=models.CASCADE, related_name='program_descr')
    content = CKEditor5Field(config_name='extends')
    slug = models.SlugField()

    def save(self, **kwargs):
        self.slug = slugify(self.title_link)
        super(ProgramModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'


