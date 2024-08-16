from django.shortcuts import render, get_object_or_404
from ..models import Projects


def render_personal_profile(request):
    """
    This function will return the resume page of the website.
    Page with my resume.
    """
    projects = Projects()
    return render(request, 'personalProfile.html', {"projects" : projects})


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
    projects = Projects.objects.all()
    return render(request, 'projects.html', {"projects": projects})


def render_single_project(request, pk):
    """
    renders project alone  with details.
    """
    project = get_object_or_404(Projects, pk=pk)
    # or
    # project = Projects.objects.get.(id=pk)
    return render(request, "project.html", {"project": project})


