from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import JournalModel, Site


class JournalViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com', name='hamidehsakak.com')
        return super(JournalViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['journal:journal_list']

    def location(self, item):
        return '/blog'


class JournalSnippetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='hamidehsakak.com', name='hamidehsakak.com')
        return super(JournalSnippetSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return JournalModel.objects.all()

