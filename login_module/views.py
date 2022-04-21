from django.shortcuts import render

# Create your views here.


def login(req):
    return render(req, 'login_module/login_page.html', {})
