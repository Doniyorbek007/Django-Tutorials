from django.db import models

# Create your models here.
class Price(models.Model):
    photo = models.ImageField(upload_to='media',unique=True)
    starting = models.FloatField(max_length=6)
    haircut = models.FloatField(max_length=6)
    beard_trim = models.FloatField(max_length=6)
    razor_cut = models.FloatField(max_length=6)
    shawes = models.FloatField(max_length=6)
    styling_color = models.FloatField(max_length=6)


class Contact(models.Model):
    open_time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)

class Branche(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
