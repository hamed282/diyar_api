from django.db import models


class JournalModel(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='images/journal/')
    content_up = models.TextField(max_length=4000)
    content_button = models.TextField(max_length=4000)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
