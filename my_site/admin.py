from django.contrib import admin

from my_site.models import Article, Category, Project, Resource, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_list = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_list = ["name", "description"]


class ResourceAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name", "description")
    search_list = ["url", "name", "description"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "modified", "is_public")
    search_list = ["title", "content"]
    readonly_fields = ("slug",)
    list_filter = (
        ("is_public", admin.BooleanFieldListFilter),
        ("categories", admin.RelatedOnlyFieldListFilter),
        ("tags", admin.RelatedOnlyFieldListFilter),
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "url")
    search_list = ["title", "description", "technologies"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)
