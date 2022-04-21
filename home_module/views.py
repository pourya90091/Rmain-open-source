from django.shortcuts import render
from utils.access_check import access_check

# Create your views here.


@access_check
def home(req):
    return render(req, 'home_module/home_page.html', {})
