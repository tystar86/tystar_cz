from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Tag(models.Model):
    name = AutoSlugField(unique=True, max_length=30, populate_from=['name'])

    def __str__(self):
        return self.name


class Resource(models.Model):
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url


class Category(models.Model):
    name        = models.CharField(max_length=30)
    description = models.CharField(max_length=300, blank=True, null=True)
    slug        = AutoSlugField(unique=True, max_length=30, populate_from=['name'])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    title       = models.CharField(max_length=200, unique=True)
    content     = RichTextUploadingField()
    tag         = models.ManyToManyField(Tag, blank=True)
    category    = models.ManyToManyField(Category, blank=True)
    resource    = models.ManyToManyField(Resource, blank=True)
    likes       = models.IntegerField(default=0)
    is_public   = models.BooleanField(default=True)
    slug        = AutoSlugField(unique=True, max_length=30, populate_from=['title'])
