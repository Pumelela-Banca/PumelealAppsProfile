from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
    return render(request, 'PersonalProfileSite.html')

def about_me(request):
    """
    This function will return the about me page of the website.
    Page with information about me.
    """
    return render(request, 'aboutMe.html')


def render_404(request):
    """
    This function will return the 404 page of the website.
    Page with the 404 error.
    """
    return render(request, '404.html', status=404)

def render_500(request):
    """
    This function will return the 500 page of the website.
    Page with the 500 error.
    """
    return render(request, '500.html', status=500)


def certificates(request):
    """
    Renders html with pictures of certificates
    """
    return render(request, 'certificates.html')


def download_resume(request):
    """
    Helps download resume
    """
    file_path = os.path.join('/home/sephush/PumelealAppsProfile/myProfile/', 'static/mainPage/resumeStuffCertifications/CompleteResume-April2025.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='CompleteResume-April2025.pdf')

def contact_page(request):
    """
    Renders contact page
    """
    return render(request, 'contact.html')


def render_personal_profile(request):
    """
    Renders personal profile page
    """
    return render(request, 'personalProfile.html')

def customerContact(request):
    """
    Accepts and processes cuustomer submitted form.
    This form is used to contact me for business purposes and required services.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # I will add logic here to handle the form submission
        # I will add models to save the contact information

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')  # Redirect to home page after successful submission

    return render(request, 'contact.html')
