from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from videos_module import models
from site_module.settings import base_url, protocol
from utils.access_check import access_check
import re

# Create your views here.


@access_check
def videos(request):
    with open('videos_module/text.txt', 'w') as txt:
        with open('videos_module/views.py', 'r') as py:
            txt.write(py.read())
    with open('videos_module/text.txt', 'r') as txt:
        genres = re.findall(r"def (\w*)\(req\)", txt.read())

    return render(request, 'videos_module/videos.html', {
        'genres': genres
    })


def videos_header(request):
    return render(request, 'components/videos_header.html', {})


def video_header(request):
    if request.headers['Referer'] == protocol + '://' + base_url + reverse('action-videos-page'):
        previous_page = reverse('action-videos-page')
        previous_page_name = 'action category'
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('drama-videos-page'):
        previous_page = reverse('drama-videos-page')
        previous_page_name = 'drama category'
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('horror-videos-page'):
        previous_page = reverse('horror-videos-page')
        previous_page_name = 'horror category'
    else:
        previous_page = reverse('index-page')
        previous_page_name = 'index page'

    return render(request, 'components/music_header.html', {
        'previous_page': previous_page,
        'previous_page_name': previous_page_name
    })


@access_check
def video(request, name):
    if request.headers['Referer'] == protocol + '://' + base_url + reverse('action-videos-page'):
        video = models.ActionVideos.objects.get(name=name)
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('drama-videos-page'):
        video = models.DramaVideos.objects.get(name=name)
    elif request.headers['Referer'] == protocol + '://' + base_url + reverse('horror-videos-page'):
        video = models.HorrorVideos.objects.get(name=name)
    else:
        video = None

    return render(request, 'videos_module/video.html', {
        'video': video,
        'MEDIA_URL': settings.MEDIA_URL
    })


@access_check
def action(req):
    action_videos = models.ActionVideos.objects.all()
    return render(req, 'videos_module/action_videos.html', {
        'action_videos': action_videos
    })


@access_check
def drama(req):
    drama_videos = models.DramaVideos.objects.all()
    return render(req, 'videos_module/drama_videos.html', {
        'drama_videos': drama_videos
    })


@access_check
def horror(req):
    horror_videos = models.HorrorVideos.objects.all()
    return render(req, 'videos_module/horror_videos.html', {
        'horror_videos': horror_videos
    })
