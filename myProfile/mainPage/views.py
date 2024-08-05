from django.shortcuts import render

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
