from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class Resource(models.Model):
    url = models.URLField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from=["title"])

    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.title
