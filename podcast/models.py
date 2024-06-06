from django.db import models
from django.utils.text import slugify


class PodcastModel(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/podcast/')
    voice = models.FileField(upload_to='voice/podcast/')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(PodcastModel, self).save(**kwargs)

    class Meta:
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcast'

    def get_absolute_url(self):
        return f'/{self.slug}'


class Site(models.Model):
    domain = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
