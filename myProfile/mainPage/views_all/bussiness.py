from django.shortcuts import render, get_object_or_404
from ..models import Projects, Services



def render_bussiness_profile(request):
    """
    This function will return the bussiness profile page of the website.
    Page with my bussiness profile.
    """
    services = Services.objects.all()
    return render(request, 'bussinessProfile.html', {"services": services})

def render_services(request):
    """
    Renders the services that I offer
    """
    services = Services.objects.all()
    return render(request, "", {"servives": services})

def render_service_and_form(request, pk):
    """
    renders service's page and form to ask questions and apply
    """
    pass
