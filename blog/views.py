from django.shortcuts import render, redirect


def index(request):
    context = {
    }
    return render(request, 'blog/index.html', context)
