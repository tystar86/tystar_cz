from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from my_site.models import Article, Category, Tag


BASE_CONTEXT = {
    "name": "Štěpánka",
    "surname": "Lucinová",
    "email": "stepankalucinova@gmail.com",
    # "twitter": "https://twitter.com/tystarcz",
    "linkedin": "https://www.linkedin.com/in/stepankalucinova/",
    "github": "https://github.com/tystar86",
    # "hackerrank": "https://www.hackerrank.com/tystar",
    # "couchsurfing": "https://www.couchsurfing.com/people/stepanka.stephanie",
    "instagram": "https://www.instagram.com/stepanka.stephanie/",
}


class Homepage(TemplateView):
    template_name = "homepage.html"


class About(TemplateView):
    template_name = "about.html"


class BlogHomepage(ListView):
    model = Article
    template_name = "blog_homepage.html"

    def get_context_data(self):
        latest_articles = Article.objects.all()
        categories = []
        context = {"latest_articles": latest_articles, "categories": categories, **BASE_CONTEXT}
        return context
    

class ArticleView(DetailView):
    model = Article
    template_name = "article.html"


class CategoryView(DetailView):
    model = Category
    template_name = "category.html"


class TagView(DetailView):
    model = Tag
    template_name = "tag.html"
