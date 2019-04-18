from django.conf.urls import url

from .views import index, post, category, tag


app_name = 'blog'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^post/(?P<post_slug>[\w\-]+)/$', post, name='post'),
    url(r'^category/(?P<category_slug>[\w\-]+)/$', category, name='category'),
    url(r'^tag/(?P<tag_slug>[\w\-]+)/$', tag, name='tag'),
]
