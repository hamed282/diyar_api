from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import BaseHomeModel, Site


class HomeViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com', name='hamidehsakak.com')
        return super(HomeViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['home:home']

    def location(self, item):
        return ''


class HomeSnippetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com/podcast', name='hamidehsakak.com/podcast')
        return super(HomeSnippetSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return BaseHomeModel.objects.all()

    def lastmod(self, item):
        return item.updated

