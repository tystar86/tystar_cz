from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=30)
    url  = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name        = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    slug        = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    title       = models.CharField(max_length=50, unique=True)
    text        = models.TextField()
    tag         = models.ManyToManyField(Tag, blank=True)
    category    = models.ManyToManyField(Category, blank=True)
    resource      = models.ManyToManyField(Resource, blank=True)
    likes       = models.IntegerField(default=0)
    is_public   = models.BooleanField(default=True)

    slug        = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
