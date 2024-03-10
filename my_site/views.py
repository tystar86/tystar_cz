from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from my_site.models import Article, Category, Project, Tag

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


class Portfolio(ListView):
    model = Project
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        projects = Project.objects.all()

        return {"projects": projects, **BASE_CONTEXT}


class BlogHomepage(ListView):
    model = Article
    template_name = "blog_homepage.html"

    def get_context_data(self, **kwargs):
        latest_articles = Article.objects.all()
        categories = []  # TODO: display categories
        tags = []  # TODO: display tags
        resources = []  # TODO: display resources

        return {
            "latest_articles": latest_articles,
            "categories": categories,
            "tags": tags,
            "resources": resources,
            **BASE_CONTEXT,
        }


class ArticleView(DetailView):
    model = Article
    template_name = "article.html"


class CategoryView(DetailView):
    model = Category
    template_name = "category.html"


class TagView(DetailView):
    model = Tag
    template_name = "tag.html"
