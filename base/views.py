from django.shortcuts import render

from blog.models import Resource


def homepage(request):
    resources = Resource.objects.all()
    context = {
        'name': 'Štěpánka',
        'surname': 'Lucinová',
        'email': 'stepankalucinova@gmail.com',
        'twitter': 'https://twitter.com/tystarcz',
        'linkedin': 'https://www.linkedin.com/in/stepankalucinova/',
        'github': 'https://github.com/tystar86',
        'resources': resources,
    }
    return render(request, 'homepage.html', context)


def about(request):
    return render(request, 'about.html')
