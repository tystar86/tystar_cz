from django.contrib import admin
from my_site.models import Article, Resource


class ResourceAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name", "description")
    search_list = ["url", "name", "description"]

admin.site.register(Resource, ResourceAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "modified", "is_public")
    search_list = ["title", "content"]
    list_filter = (
        ("is_public", admin.BooleanFieldListFilter),
        # ("categories", admin.RelatedOnlyFieldListFilter),
        # ("tags", admin.RelatedOnlyFieldListFilter),
    )

admin.site.register(Article, ArticleAdmin)