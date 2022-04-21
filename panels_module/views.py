from django.shortcuts import render
from django.conf import settings
from django.utils.crypto import get_random_string
from login_module.models import Users
from utils.access_check import access_check

# Create your views here.


@access_check
def panel(req, panel_slug):
    try:
        user = Users.objects.get(username=panel_slug)
    except:
        user = False
    if user:
        return render(req, 'panels_module/panel_page.html', {
            'user': user,
            'MEDIA_URL': settings.MEDIA_URL
        })
    else:
        return render(req, '404.html', {})


@access_check
def edit_account(req, panel_slug):
    try:
        user = Users.objects.get(username=panel_slug)
    except:
        user = False
    if user:
        return render(req, 'panels_module/edit_account_page.html', {
            'user': user,
            'MEDIA_URL': settings.MEDIA_URL
        })
    else:
        return render(req, '404.html', {})


@access_check
def delete_account(req, panel_slug):
    try:
        user = Users.objects.get(username=panel_slug)
    except:
        user = False
    if user:
        return render(req, 'panels_module/delete_account_page.html', {
            'user': user,
            'MEDIA_URL': settings.MEDIA_URL
        })
    else:
        return render(req, '404.html', {})


@access_check
def email_verification(req, panel_slug):
    try:
        user = Users.objects.get(username=panel_slug)
    except:
        user = False
    if user:
        return render(req, 'panels_module/email_verification_page.html', {
            'user': user,
            'MEDIA_URL': settings.MEDIA_URL
        })
    else:
        return render(req, '404.html', {})


def email_verification_code(req, panel_slug, code):
    try:
        user = Users.objects.get(username=panel_slug)
    except:
        user = False
    if user.verification_code == code:
        error = ''
        if user.verification_code == code:
            if user.is_active is False:
                user.is_active = True
                user.verification_code = get_random_string(72)
                user.save()
            else:
                error = 'email already verified'
        else:
            error = 'verification code not valid'
        return render(req, 'panels_module/email_verification_code_page.html', {
            'user': user,
            'MEDIA_URL': settings.MEDIA_URL,
            'error': error
        })
    else:
        return render(req, '404.html', {})


def recover_password(req):
    return render(req, 'panels_module/recover_password_page.html', {})


def ACP(req, code):
    if req.method == "GET":
        try:
            print(f"code: {code}")
            Users.objects.get(verification_code=code)
        except Exception as err:
            print(err)
            return render(req, '404.html', {})
        return render(req, 'panels_module/set_new_password_page.html', {})
    else:
        return render(req, 'login_module/login_page.html')
