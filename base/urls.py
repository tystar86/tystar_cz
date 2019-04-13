from django.conf.urls import url

from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control

from base.views import homepage, about
from tystar_cz.settings import base

urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'about/$', about, name='about'),
]


if base.DEBUG:
    urlpatterns += static(base.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))
