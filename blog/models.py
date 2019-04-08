from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    name        = models.CharField(max_length=30)
    description = models.CharField(max_length=300)


class Post(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    title       = models.CharField(max_length=50, unique=True)
    text        = models.TextField()
    tags        = models.ManyToManyField(Tag)
    category    = models.ManyToManyField(Category)
    is_public   = models.BooleanField(default=True)
