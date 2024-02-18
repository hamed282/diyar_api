from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class JournalModel(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='images/journal/')
    description = models.TextField()
    content = CKEditor5Field(config_name='extends')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.slug}'
