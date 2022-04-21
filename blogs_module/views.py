from django.shortcuts import render
from blogs_module.models import Jokes
from utils.access_check import access_check
import re

# Create your views here.


@access_check
def blogs(request):
    with open('blogs_module/text.txt', 'w') as txt:
        with open('blogs_module/views.py', 'r') as py:
            txt.write(py.read())
    with open('blogs_module/text.txt', 'r') as txt:
        blogs = re.findall(r"def (\w*)\(req\)", txt.read())

    return render(request, 'blogs_module/blogs.html', {
        'blogs': blogs,
    })


def blogs_header(request):
    return render(request, 'components/blogs_header.html', {})


@access_check
def joke(req):
    jokes = Jokes.objects.all()[:5]

    return render(req, 'blogs_module/joke_page.html', {
        'jokes': jokes
    })


@access_check
def weather(req):
    return render(req, 'blogs_module/weather_page.html', {})


@access_check
def resume(req):
    return render(req, 'blogs_module/resume.html', {})
