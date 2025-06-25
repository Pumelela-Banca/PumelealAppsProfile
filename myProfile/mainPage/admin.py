from django.contrib import admin
from .models import Projects, Services, ContactUs

# Register your models here.

admin.site.register(Projects)
admin.site.register(Services)
admin.site.register(ContactUs)
