"""
URL configuration for myProfile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from mainPage.views import (render_personal_profile, render_home_page,
                            render_bussiness_profile, about_me, render_resume,
                            render_projects, render_single_project,
                            render_services, ServiceDetailView,
                            ServicesListView, render_404, certificates, download_resume,
                            contact_page, render_500, customerContact, render_apps_downloads_page,
                            download_shortcut_app, render_catch_items_game)
from django.conf.urls import handler404, handler500


handler404 = render_404
handler500 = render_500
urlpatterns = [
    path("", render_home_page, name="home"),
    path("personalProfile/", render_personal_profile, name="personalProfile"),
    path("aboutMe/", about_me, name="aboutMe"),
    path("resume/", render_resume, name="resume"),
    path('projects/', render_projects, name='projects'),
    #path('services', ServicesListView.as_view(), name="services"),
    path('services/<int:pk>', ServiceDetailView.as_view(), name="service"),
    path('certificates/', certificates, name="certificates"),
    path('download_resume/', download_resume, name="download_resume"),
    path('contact/', contact_page, name="contact"), 
    path("customerContact/", customerContact, name="customerContact"),
    path("Download/", render_apps_downloads_page, name="apps_page"),
    # Versioned URLs for projects
    path("Download/ShortCutApp/1.1", download_shortcut_app, name="download_ShortCutApp"),
    path("Games/catchBusket", render_catch_items_game, name="catch_items_game"),
]
