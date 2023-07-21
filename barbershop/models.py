from django.db import models

# Create your models here.
class Contact(models.Model):
    open_time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)

    
    street = models.CharField(max_length=255)
    location = models.CharField(max_length=255)