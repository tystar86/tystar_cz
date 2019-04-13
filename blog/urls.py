from django.conf.urls import url

from .views import index, post, category


app_name = 'blog'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^post/(?P<post_slug>[\w\-]+)/$', post, name='article'),
    url(r'category/(?P<category_slug>[\w\-]+)/$', category, name='category'),
]
