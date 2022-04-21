from django.shortcuts import render
from utils.access_check import access_check
import re

# Create your views here.


@access_check
def games(request):
    with open('games_module/text.txt', 'w') as txt:
        with open('games_module/views.py', 'r') as py:
            txt.write(py.read())
    with open('games_module/text.txt', 'r') as txt:
        games = re.findall(r"def (\w*)\(req\)", txt.read())

    return render(request, 'games_module/games.html', {
        'games': games
    })


def games_header(request):
    return render(request, 'components/games_header.html', {})


@access_check
def HJ_game(req):
    return render(req, 'games_module/HJ_game.html', {})


@access_check
def tetris(req):
    return render(req, 'games_module/tetris/canvas-tetris/index.html', {})


@access_check
def game2048(req):
    return render(req, 'games_module/2048/2048/index.html', {})
