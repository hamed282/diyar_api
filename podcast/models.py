from django.db import models


class PodcastModel(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/podcast/')
    voice = models.FileField(upload_to='voice/podcast/')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcast'
