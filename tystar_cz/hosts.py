from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'', 'base.urls', name='base'),
    host(r'blog', 'blog.urls', name='blog'),
)
