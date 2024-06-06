from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import CategoryProgramModel, SubCategoryProgramModel, Site


class ProgramViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com', name='hamidehsakak.com')
        return super(ProgramViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['programs:category_list']

    def location(self, item):
        return '/program'


class CategoryProgramSnippetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com/program', name='hamidehsakak.com/program')
        return super(CategoryProgramSnippetSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return CategoryProgramModel.objects.all()

    def lastmod(self, item):
        return item.updated


class SubcategoryProgramSnippetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com', name='hamidehsakak.com')
        return super(SubcategoryProgramSnippetSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return SubCategoryProgramModel.objects.all()

    def location(self, item):
        return f'/program/{item.category}/{item.slug}'

    def lastmod(self, item):
        return item.updated
