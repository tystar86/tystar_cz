from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField



class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(unique=True, max_length=30, populate_from=["name"])

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300, blank=True)
    slug = AutoSlugField(unique=True, max_length=30, populate_from=["name"])

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"


class Resource(models.Model):
    url = models.URLField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    is_public = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from=["title"])

    resources = models.ManyToManyField(Resource, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
