from django.shortcuts import render


def homepage(request):
    context = {
        'about_url': 'about/',
        'contact_url': 'contact/',
    }
    return render(request, 'homepage.html', context)


def about(request):
    context = {
        'homepage_url': '/',
        'contact_url': 'contact/',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'name': 'Štěpánka',
        'surname': 'Lucinová',
        'email': 'stepankalucinova@gmail.com',
        'homepage_url': '/',
        'about_url': 'about/',
    }
    return render(request, 'contact.html', context)
