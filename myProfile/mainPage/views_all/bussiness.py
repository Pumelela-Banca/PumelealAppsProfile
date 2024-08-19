from django.shortcuts import render
from ..models import Services
from django.views.generic.list import ListView
from django.views.generic import DetailView


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
    return render(request, "services.html", {"services": services})


class ServicesListView(ListView):
    """
    Renders services page
    """
    template_name = "services.html"
    model = Services
    paginate_by = 5

    def get_queryset(self):
        queryset = Services.objects.all().order_by("name")
        return queryset


class ServiceDetailView(DetailView):
    """
    Renders services Details
    """
    model = Services
    template_name = "service.html"


