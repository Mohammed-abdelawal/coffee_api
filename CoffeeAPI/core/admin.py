from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.CoffeeMachine)
admin.site.register(models.CoffeePod)