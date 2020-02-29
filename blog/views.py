from django.shortcuts import render

posts = [
    {
        'author': 'Julio',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nam similique sunt, nulla repudiandae sequi rem minus facilis, culpa molestiae beatae consectetur illum in harum voluptatem fuga reprehenderit. Exercitationem, a. Consequuntur.',
        'date_posted': '29-02-2020'
    },
    {
        'author': 'Julio',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nam similique sunt, nulla repudiandae sequi rem minus facilis, culpa molestiae beatae consectetur illum in harum voluptatem fuga reprehenderit. Exercitationem, a. Consequuntur.',
        'date_posted': '29-02-2020'
    },
    {
        'author': 'Julio',
        'title': 'Blog Post 3',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nam similique sunt, nulla repudiandae sequi rem minus facilis, culpa molestiae beatae consectetur illum in harum voluptatem fuga reprehenderit. Exercitationem, a. Consequuntur.',
        'date_posted': '29-02-2020'
    }
]

# render looks inside the templates directory

def home(request):
    context = {
        'posts': posts,
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
