from django.db import models

# Create your models here.

class AboutUs(models.Model):
    Image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField()
    
