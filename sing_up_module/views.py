from django.shortcuts import render


# Create your views here.


def sing_up(req):
    return render(req, 'sing_up_module/sing_up_page.html', {})
