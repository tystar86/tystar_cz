from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name        = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    title       = models.CharField(max_length=50, unique=True)
    text        = models.TextField()
    tag         = models.ManyToManyField(Tag, blank=True, null=True)
    category    = models.ManyToManyField(Category, blank=True, null=True)
    like        = models.IntegerField(default=0)
    is_public   = models.BooleanField(default=True)
