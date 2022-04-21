from django.shortcuts import render
from login_module.models import Users
from django.http import Http404
import re


def access_check(function_view):
    def wrapper(req, *args, **kwargs):
        if 'Cookie' in req.headers:
            username = re.findall(r"access_token=(.+)", req.headers['Cookie'])
            if len(username) == 1:
                try:
                    Users.objects.get(username=username[0])
                    if 'panel_slug' in kwargs:
                        if username[0] != kwargs['panel_slug']:
                            raise Exception
                except:
                    raise Http404()
                else:
                    return function_view(req, *args, **kwargs)
        raise Http404()
    return wrapper


def access_header(function_view):
    def wrapper(req, *args, **kwargs):
        if 'Cookie' in req.headers:
            username = re.findall(r"access_token=(.+)", req.headers['Cookie'])
            if len(username) == 1:
                try:
                    Users.objects.get(username=username[0])
                except:
                    return render(req, 'components/header.html', {'logged_in': False})
                else:
                    return function_view(req, *args, **kwargs)
        return render(req, 'components/header.html', {'logged_in': False})
    return wrapper
