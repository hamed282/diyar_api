from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import PodcastModel, Site


class PodcastViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com', name='hamidehsakak.com')
        return super(PodcastViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['podcast:podcast']

    def location(self, item):
        return '/podcast'


class PodcastSnippetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com/podcast', name='hamidehsakak.com/podcast')
        return super(PodcastSnippetSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return PodcastModel.objects.all()

