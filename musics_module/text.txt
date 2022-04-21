from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from musics_module import models
from site_module.settings import base_url, protocol
from utils.access_check import access_check
import re

# Create your views here.


@access_check
def musics(request):
    with open('musics_module/text.txt', 'w') as txt:
        with open('musics_module/views.py', 'r') as py:
            txt.write(py.read())
    with open('musics_module/text.txt', 'r') as txt:
        genres = re.findall(r"def (\w*)\(req\)", txt.read())

    return render(request, 'musics_module/musics.html', {
        'genres': genres
    })


def musics_header(request):
    return render(request, 'components/musics_header.html', {})


def music_header(request):
    if request.headers['Referer'] == protocol + '://' + base_url + reverse('sad-musics-page'):
        previous_page = reverse('sad-musics-page')
        previous_page_name = 'sad category'
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('hype-musics-page'):
        previous_page = reverse('hype-musics-page')
        previous_page_name = 'hype category'
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('old-musics-page'):
        previous_page = reverse('old-musics-page')
        previous_page_name = 'old category'
    else:
        previous_page = reverse('index-page')
        previous_page_name = 'index page'

    return render(request, 'components/music_header.html', {
        'previous_page': previous_page,
        'previous_page_name': previous_page_name
    })


@access_check
def music(request, name):
    if request.headers['Referer'] == protocol + '://' + base_url + reverse('sad-musics-page'):
        music = models.SadMusics.objects.get(name=name)
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('hype-musics-page'):
        music = models.HypeMusics.objects.get(name=name)
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('old-musics-page'):
        music = models.OldMusics.objects.get(name=name)
    else:
        music = None

    return render(request, 'musics_module/music.html', {
        'music': music,
        'MEDIA_URL': settings.MEDIA_URL
    })


@access_check
def sad(req):
    sad_musics = models.SadMusics.objects.all()
    return render(req, 'musics_module/sad_musics.html', {
        'sad_musics': sad_musics
    })


@access_check
def hype(req):
    hype_musics = models.HypeMusics.objects.all()
    return render(req, 'musics_module/hype_musics.html', {
        'hype_musics': hype_musics
    })


@access_check
def old(req):
    old_musics = models.OldMusics.objects.all()
    return render(req, 'musics_module/old_musics.html', {
        'old_musics': old_musics
    })
