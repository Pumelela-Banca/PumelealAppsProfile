from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Projects, Services, ContactUs
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
    return render(request, 'personalProfileSite.html')

def about_me(request):
    """
    This function will return the about me page of the website.
    Page with information about me.
    """
    return render(request, 'aboutMe.html')


def render_404(request, exeption):
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


def download_shortcut_app(request):
    """
    Serve the ShortCut App MSI installer based on version.
    """
    file_path = os.path.join(
        '/home/sephush/PumelealAppsProfile/myProfile/static/mainPage/ShortCutApp/',
        'ShortCutMaker.msi'  # You can change this to use version if needed
    )
    # Add version handling if necessary
   

    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='ShortCutMaker.msi')


def contact_page(request):
    """
    Renders contact page
    """
    return render(request, 'contact.html')


def render_personal_profile(request):
    """
    Renders personal profile page
    """
    return render(request, 'personalProfileSite.html')

def customerContact(request):
    """
    Accepts and processes cuustomer submitted form.
    This form is used to contact me for business purposes and required services.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        user_message = ContactUs(
            name=name,
            email=email,
            message=message
        )
        user_message.save()
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')  # Redirect to home page after successful submission

    return render(request, 'contact.html')


def render_apps_downloads_page(request):
    """
    Renders the apps downloads page.
    This page will contain links to download my apps.
    """
    return render(request, 'appsDownloads.html')


def download_app(request, app_name):
    """
    Handles the download of a specific app.
    """
    app_file_path = os.path.join('/home/sephush/PumelealAppsProfile/myProfile/static/mainPage/apps/', f'{app_name}.apk')
    
    if not os.path.exists(app_file_path):
        raise Http404("App not found")
    
    return FileResponse(open(app_file_path, 'rb'), as_attachment=True, filename=f'{app_name}.msi')


def render_projects_page(request):
    """
    Renders the projects page.
    This page will display all the projects I have worked on.
    """
    pass
    #projects = Projects.objects.all()
    #return render(request, 'projects.html', {'projects': projects})


# Games 

def render_games(request):
    """
    Reenders games page
    """
    return render(request, 'games.html')


def render_catch_items_game(request):
    """
    Renders the catch items game page.
    """
    return render(request, 'games/catchItems.html')


