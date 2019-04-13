from django.contrib import admin

from .models import Post, Tag, Category, Resource


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_list = ['name']
admin.site.register(Tag, TagAdmin)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    search_list = ['name', 'url']
admin.site.register(Resource, ResourceAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_list = ['name']
admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated', 'title', 'likes', 'is_public')
    search_list = ['title', 'source']
    list_filter = (
        ('is_public', admin.BooleanFieldListFilter),
        ('category', admin.RelatedOnlyFieldListFilter)
    )
admin.site.register(Post, PostAdmin)
