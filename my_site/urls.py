from django.urls import path, re_path

from my_site.views import Homepage, About, BlogHomepage, ArticleView, CategoryView, TagView

app_name = "my_site"

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('about/', About.as_view(), name="about"),
    path('blog/', BlogHomepage.as_view(), name="blog_homepage"),
    re_path(r"blog/article/(?P<slug>[\w\-]+)/$", ArticleView.as_view(), name="article"),

    re_path(r"category/(?P<slug>[\w\-]+)/$", CategoryView.as_view(), name="category"),
    re_path(r"tag/(?P<slug>[\w\-]+)/$", TagView.as_view(), name="tag"),
]
