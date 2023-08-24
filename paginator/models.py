from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.name