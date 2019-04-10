from django.conf.urls import url

from .views import about, homepage

urlpatterns = [
    url(r'about/$', about, name='about'),
    url(r'^$', homepage, name='homepage'),
]
