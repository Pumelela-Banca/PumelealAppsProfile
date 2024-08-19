from django.shortcuts import render, get_object_or_404
from .models import Projects, Services
from .views_all import *

# Create your views here.

def render_home_page(request):
    """
    This function will return the home page of the website.
    Page with the main information.
    """
    services = Services.objects.all()
    return render(request, 'mainPage.html', {"services": services})

def about_me(request):
    """
    This function will return the about me page of the website.
    Page with information about me.
    """
    return render(request, 'aboutMe.html')

