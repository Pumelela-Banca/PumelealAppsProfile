from django.shortcuts import render, get_object_or_404
from .models import Projects, Services
import os
from django.http import HttpResponse, Http404, FileResponse
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


def render_404(request, exception):
    """
    This function will return the 404 page of the website.
    Page with the 404 error.
    """
    return render(request, '404.html', status=404)


def certificates(request):
    """
    Renders html with pictures of certificates
    """
    return render(request, 'certificates.html')


def download_resume(request):
    """
    Helps download resume
    """
    file_path = os.path.join('/home/sephush/PumelealAppsProfile/myProfile/', 'mainPage/resumeStuffCertifications/CompleteResume-April2025.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='PumelelaInstaller.msi')

