from django.db import models


# Create your models here.


class Projects(models.Model):
    """
    Model for projects that I have done.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    url = models.URLField()
    url_video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    """
    Model of services that I offer.
    - Web Development, Cloud Solutions, Desktop Development, etc.
    """
    
    SERVICE_CATEGORIES = [
        ('Front-end', 'Web Service'),
        ('Mobile', 'Build Applications'),
        ('Web Scrapping', 'Data Collection'),
        ('Compute', 'Compute Services'),
        ('Database', 'Database Services'),
        ('Networking', 'Networking Services'),
        ('DevOps', 'Development and DevOps'),
        ('Migration', 'Migration Services'),
        ('Managed', 'Managed Services'),
        ('Support', 'Support and Consulting'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=SERVICE_CATEGORIES)
    image = models.ImageField(upload_to='mainPage/images/', null=True, blank=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    """
    Model for contact us form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.name} ({self.email})"
