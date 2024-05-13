from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from tinymce.models import HTMLField


class CategoryProgramModel(models.Model):
    objects = None
    category = models.CharField(max_length=32)
    banner = models.ImageField(upload_to='images/programs/category/banner/')
    icon = models.ImageField(upload_to='images/programs/category/icon/')

    title = models.CharField(max_length=256)
    description = HTMLField()
    # video = models.FileField(upload_to='videos/programs/category/')
    # third_description = HTMLField()
    slug = models.SlugField()

    def save(self, **kwargs):
        self.slug = slugify(self.category, allow_unicode=True)
        super(CategoryProgramModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'


class SubCategoryProgramModel(models.Model):
    objects = None
    category = models.ForeignKey(CategoryProgramModel, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=32)
    banner = models.ImageField(upload_to='images/programs/subcategory/banner/')

    title = HTMLField()

    content = HTMLField()
    description = HTMLField()
    slug = models.SlugField()

    def save(self, **kwargs):
        self.slug = slugify(self.subcategory, allow_unicode=True)
        super(SubCategoryProgramModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'


# class ProgramDescriptionModel(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#
#     def __str__(self):
#         return f'{self.title}'
#
#     class Meta:
#         verbose_name = 'Program'
#         verbose_name_plural = 'Program'
#
#
# class ProgramModel(models.Model):
#     title_link = models.CharField(max_length=100, verbose_name='Icon Title')
#     icon = models.ImageField(upload_to='images/programs/icon/')
#
#     title = models.CharField(max_length=100, verbose_name='Header')
#     description = models.OneToOneField(ProgramDescriptionModel, on_delete=models.CASCADE, related_name='program_descr')
#     # content = CKEditor5Field(config_name='extends')
#     content = HTMLField()
#     slug = models.SlugField()
#
#     def save(self, **kwargs):
#         self.slug = slugify(self.title_link, allow_unicode=True)
#         super(ProgramModel, self).save(**kwargs)
#
#     def __str__(self):
#         return f'{self.slug}'
