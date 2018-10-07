from django.shortcuts import render

from .models import Posts


def home(request):
    context = {
        'page_title': 'Home',
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'page_title': 'About'
    }
    return render(request, 'blog/about.html', context)
