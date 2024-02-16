from django.db import models


class ProgramListModel(models.Model):
    program = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='images/programs/')
    slug = models.SlugField()
