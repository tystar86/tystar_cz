from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Post, Category, Tag


_BASE_CONTEXT = {
        'name': 'Štěpánka',
        'surname': 'Lucinová',
        'email': 'stepankalucinova@gmail.com',
        'twitter': 'https://twitter.com/tystarcz',
        'linkedin': 'https://www.linkedin.com/in/stepankalucinova/',
        'github': 'https://github.com/tystar86',
    }
def index(request):
    latest_posts_list = Post.objects.filter(is_public=True).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_posts_list, 10)

    try:
        latest_posts = paginator.page(page)
    except PageNotAnInteger:
        latest_posts = paginator.page(1)
    except EmptyPage:
        latest_posts = paginator.page(paginator.num_pages)

    context = {
        'latest_posts': latest_posts,
    }
    context = {**context, **_BASE_CONTEXT}

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


def tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    context = {
        'tag': tag,
    }

    return render(request, 'blog/tag.html', context)

# from django.db.models import Count
#    top_categories = Category.objects.annotate(num_posts=Count('post')).order_by('-num_posts')[:5]
