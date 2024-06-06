from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from tinymce.models import HTMLField


class CategoryTagModel(models.Model):
    objects = None
    tag = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category Tag'
        verbose_name_plural = 'categories Tag'

    # def save(self, **kwargs):
    #     self.slug = slugify(self.tag)
    #     super(TagModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.tag}'


class CategoryProgramModel(models.Model):
    objects = None
    category = models.CharField(max_length=32)
    banner = models.ImageField(upload_to='images/programs/category/banner/')
    icon = models.ImageField(upload_to='images/programs/category/icon/')

    title = models.CharField(max_length=256)
    description = HTMLField()
    # video = models.FileField(upload_to='videos/programs/category/')
    # third_description = HTMLField()
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=150)

    slug = models.SlugField(allow_unicode=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # def save(self, **kwargs):
    #     self.slug = slugify(self.category, allow_unicode=True)
    #     super(CategoryProgramModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'

    def get_absolute_url(self):
        return f'/{self.slug}'


class AddCategoryTagModel(models.Model):
    objects = None
    tag = models.OneToOneField(CategoryTagModel, on_delete=models.CASCADE, unique=True)
    journal = models.ForeignKey(CategoryProgramModel, on_delete=models.CASCADE, related_name='category_tag')

    def __str__(self):
        return f'{self.tag}'


class SubcategoryTagModel(models.Model):
    objects = None
    tag = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Subcategory Tag'
        verbose_name_plural = 'Subcategories Tag'

    # def save(self, **kwargs):
    #     self.slug = slugify(self.tag)
    #     super(TagModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.tag}'


class SubCategoryProgramModel(models.Model):
    objects = None
    category = models.ForeignKey(CategoryProgramModel, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=32)
    media = models.FileField(upload_to='media/programs/subcategory/')
    banner = models.ImageField(upload_to='images/programs/subcategory/banner/')

    title = HTMLField()

    content = HTMLField()
    # description = HTMLField()

    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=150)

    slug = models.SlugField(allow_unicode=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # def save(self, **kwargs):
    #     self.slug = slugify(self.subcategory, allow_unicode=True)
    #     super(SubCategoryProgramModel, self).save(**kwargs)

    def __str__(self):
        return f'{self.slug}'

    def get_absolute_url(self):
        return f'/{self.slug}'


class AddSubcategoryTagModel(models.Model):
    objects = None
    tag = models.OneToOneField(SubcategoryTagModel, on_delete=models.CASCADE, unique=True)
    journal = models.ForeignKey(CategoryProgramModel, on_delete=models.CASCADE, related_name='subcategory_tag')

    def __str__(self):
        return f'{self.tag}'


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


class Site(models.Model):
    domain = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
