from django.shortcuts import render


def index(request):
    context = {
        'homepage_url': '/',
        'about_url': 'about/',
    }
    return render(request, 'blog/index.html', context)
