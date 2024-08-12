from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.

def render_home_page(request):
    """
    This function will return the home page of the website.
    Page with the main information.
    """
    return render(request, 'layout.html')

def render_personal_profile(request):
    """
    This function will return the resume page of the website.
    Page with my resume.
    """
    return render(request, 'personalProfile.html')

def render_bussiness_profile(request):
    """
    This function will return the bussiness profile page of the website.
    Page with my bussiness profile.
    """
    return render(request, 'bussinessProfile.html')

def about_me(request):
    """
    This function will return the about me page of the website.
    Page with information about me.
    """
    return render(request, 'aboutMe.html')

def render_resume(request):
    """
    This function will return the resume page of the website.
    Page with my resume.
    """
    return render(request, 'resume.html')

def render_projects(request):
    """
    This function will return the projects page of the website.
    Page with my projects.
    """
    projects = Projects()
    return render(request, 'projects.html', {"projects": projects})

def render_single_project(request, pk):
    """
    renders project alone  with details.
    """
    project = get_object_or_404(Projects, pk=pk)
    render(request, "project.html", {"project": project})

