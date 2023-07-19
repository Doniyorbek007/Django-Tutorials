from django.db import models

# Create your models here.
class Contact(models.Model):
    open_time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    social_media = models.CharField(max_length=255)