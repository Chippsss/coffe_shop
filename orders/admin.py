from django.contrib import admin

# Register your models here.
from .models import Order, MenuItem

admin.site.register(Order)
admin.site.register(MenuItem)