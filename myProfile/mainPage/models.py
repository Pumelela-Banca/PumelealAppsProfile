from django.db import models

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name
