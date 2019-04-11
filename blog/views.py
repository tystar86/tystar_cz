from django.shortcuts import render

from django.db.models import Sum, Count

from .models import Post, Category, Tag


def index(request):
    latest_posts = Post.objects.order_by('created')[5]
    top_posts = Post.objects.order_by('like')[5]
    import ipdb;ipdb.set_trace
    top_categories = Category.objects. \
        annotate(num_posts=Count('post')) \
        .order_by('-num_posts')[5]
    top_tags = Tag.objects \
        .annotate(num_posts=Count('post')) \
        .order_by('-num_posts')[5]

    context = {
        'latest_posts': latest_posts,
        'top_posts': top_posts,
        'top_categories': top_categories,
        'top_tags': top_tags,
    }
    return render(request, 'blog/index.html', context)
