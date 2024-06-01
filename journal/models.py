from django.db import models
# from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from tinymce.models import HTMLField


class TagModel(models.Model):
    objects = None
    tag = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Journal Tag'
        verbose_name_plural = 'Journal Tag'

    # def save(self, **kwargs):
    #     self.slug = slugify(self.tag)
    #     super(TagModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.tag}'


class JournalModel(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='images/journal/')
    description = models.CharField(max_length=200)
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256)
    # content = CKEditor5Field(config_name='extends')
    content = HTMLField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    slug = models.SlugField()

    # def save(self, **kwargs):
    #     self.slug = slugify(self.title, allow_unicode=True)
    #     super(JournalModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journal'


class AddTagModel(models.Model):
    objects = None
    tag = models.ForeignKey(TagModel, on_delete=models.CASCADE)
    journal = models.ForeignKey(JournalModel, on_delete=models.CASCADE, related_name='journal_tag')

    def __str__(self):
        return f'{self.tag}'
