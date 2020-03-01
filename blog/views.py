from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Blog - Home',
        'meta': {
            'title': 'Title home page',
            'description': 'Description home page',
        }
    }

    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'Blog - About',
        'meta': {
            'title': 'Title about page',
            'description': 'Description About page',
        }
    }

    return render(request, 'blog/about.html', context)
