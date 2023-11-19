from django.urls import path, re_path

from my_site.views import Homepage, About, BlogHomepage, ArticleView

app_name = "my_site"

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('about/', About.as_view(), name="about"),
    path('blog/', BlogHomepage.as_view(), name="blog_homepage"),
    re_path(r"blog/article/(?P<pk>\d+)$", ArticleView.as_view(), name="blog_article_detail"),
]
