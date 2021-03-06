from django.shortcuts import render

from blog.models import Resource


_BASE_CONTEXT = {
    'name': 'Štěpánka',
    'surname': 'Lucinová',
    'email': 'stepankalucinova@gmail.com',
    'twitter': 'https://twitter.com/tystarcz',
    'linkedin': 'https://www.linkedin.com/in/stepankalucinova/',
    'github': 'https://github.com/tystar86',
    'hackerrank': 'https://www.hackerrank.com/tystar',
    'couchsurfing': 'https://www.couchsurfing.com/people/stepanka.stephanie',
    'instagram': 'https://www.instagram.com/stepanka.stephanie/',
    }
def homepage(request):
    resources = Resource.objects.exclude(name=None)
    context = {
        'resources': resources,
    }
    context = {**context, **_BASE_CONTEXT}

    return render(request, 'homepage.html', context)


def about(request):
    return render(request, 'about.html', _BASE_CONTEXT)
