from django.db import models


class AnswerRecommenderModel(models.Model):
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    a3 = models.IntegerField()
    a4 = models.IntegerField()
    a5 = models.IntegerField()
    a6 = models.IntegerField()
    a7 = models.IntegerField()
    a8 = models.IntegerField()
    a9 = models.IntegerField()
    a10 = models.IntegerField()
    a11 = models.IntegerField()
    a12 = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
