from django.shortcuts import render
from ..models import Services
from django.views.generic.list import ListView, CreateView


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
    return render(request, "services.html", {"servives": services})


class ServicesListView(ListView):
    """
    Renders services page
    """
    template_name = "services.html"
    model = Services

    def get_queryset(self):
        queryset = Services.objects.all().order_by("name")
        return queryset
    

def render_service_and_form(request, pk):
    """
    renders service's page and form to ask questions and apply
    """
    pass
