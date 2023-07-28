from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Contact)
admin.site.register(Branche)
admin.site.register(Price)
admin.site.register(Service)
admin.site.register(Barber)