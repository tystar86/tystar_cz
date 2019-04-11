from django.conf.urls import url

from .views import index, list_categories, list_tags, add_category


app_name = 'blog'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^categories/$', list_categories, name='list_categories'),
    url(r'^categories/add_category/', add_category, name='add_category'),
    url(r'^tags/$', list_tags, name='list_tags'),
]
