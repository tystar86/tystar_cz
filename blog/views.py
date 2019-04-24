from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Post, Category, Tag
from base.views import _BASE_CONTEXT


def index(request):
    latest_posts_list = Post.objects.filter(is_public=True).order_by('-created')
    categories = Category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_posts_list, 8)

    try:
        latest_posts = paginator.page(page)
    except PageNotAnInteger:
        latest_posts = paginator.page(1)
    except EmptyPage:
        latest_posts = paginator.page(paginator.num_pages)

    context = {
        'latest_posts': latest_posts,
        'categories': categories,
    }
    context = {**context, **_BASE_CONTEXT}

    return render(request, 'blog/index.html', context)


def post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {
        'post': post,
    }
    context = {**context, **_BASE_CONTEXT}

    return render(request, 'blog/post.html', context)


def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'category': category,
    }
    context = {**context, **_BASE_CONTEXT}

    return render(request, 'blog/category.html', context)


def tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    context = {
        'tag': tag,
    }
    context = {**context, **_BASE_CONTEXT}

    return render(request, 'blog/tag.html', context)

# from django.db.models import Count
#    top_categories = Category.objects.annotate(num_posts=Count('post')).order_by('-num_posts')[:5]
