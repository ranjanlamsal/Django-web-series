from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title