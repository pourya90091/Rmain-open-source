from django.shortcuts import render
from utils.access_check import access_header

# Create your views here.


def index(req):
    return render(req, 'index.html', {})


# partial view
@access_header
def header(req):
    return render(req, 'components/header.html', {'logged_in': True})


def footer(req):
    return render(req, 'components/footer.html', {})
