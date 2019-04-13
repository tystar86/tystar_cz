from django.shortcuts import render

from .models import Post, Category


def index(request):
    latest_posts = Post.objects.order_by('created')

    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/index.html', context)


def post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)


def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'category': category,
    }
    return render(request, 'blog/category.html', context)

# from django.db.models import Count
#    top_categories = Category.objects.annotate(num_posts=Count('post')).order_by('-num_posts')[:5]
