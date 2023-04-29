from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank= False)
    image = models.ImageField(upload_to='images/blog', blank=True)