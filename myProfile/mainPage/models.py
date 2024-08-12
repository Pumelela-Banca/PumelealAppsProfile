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

    def __str__(self):
        return self.name


class Services(models.Model):
    """
    Model of services that I offer.
    - Web Development, Cloud Solutions, Desktop Development, etc.
    """
    
    SERVICE_CATEGORIES = [
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

    def __str__(self):
        return self.name
