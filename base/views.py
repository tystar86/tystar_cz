from django.shortcuts import render


def homepage(request):
    context = {
        'homepage_url': '/',
        'about_url': 'about/',
    }
    return render(request, 'homepage.html', context)


def about(request):
    context = {
        'homepage_url': '/',
        'about_url': 'about/',
        'name': 'Štěpánka',
        'surname': 'Lucinová',
        'email': 'stepankalucinova@gmail.com',
    }
    return render(request, 'about.html', context)
