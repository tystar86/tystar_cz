from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'www', 'base.urls', name='www'),
    host(r'blog', 'blog.urls', name='blog'),
    #host(r'prdel', 'prdel.url', name='prdel'),
    #host(r'tmdb', 'base.url', name='tmdb'),
)
