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
from django.contrib import admin
from django.urls import path
from mainPage.views import (render_personal_profile, render_home_page,
                            render_bussiness_profile, about_me, render_resume,
                            render_projects, render_single_project,
                            render_services, render_service_and_form)

urlpatterns = [
    path("", render_home_page, name="home"),
    path("personalProfile/", render_personal_profile, name="personalProfile"),
    path("bussinessProfile/", render_bussiness_profile, name="bussinessProfile"),
    path("aboutMe/", about_me, name="aboutMe"),
    path("resume/", render_resume, name="resume"),
    path('projects/', render_projects, name='projects'),
    path('projects/<int:pk>', render_single_project, name="project"),
    path('services', render_services, name="services"),
    path('services/<int:pk>', render_service_and_form, name="service"),
]
