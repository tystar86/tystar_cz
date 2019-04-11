from django.shortcuts import render


def homepage(request):
    context = {
    }
    return render(request, 'homepage.html', context)


def about(request):
    context = {
        'name': 'Štěpánka',
        'surname': 'Lucinová',
        'email': 'stepankalucinova@gmail.com',
        'twitter': 'https://twitter.com/tystarcz',
        'linkedin': 'https://www.linkedin.com/in/stepankalucinova/',
        'github': 'https://github.com/tystar86',
    }
    return render(request, 'about.html', context)
