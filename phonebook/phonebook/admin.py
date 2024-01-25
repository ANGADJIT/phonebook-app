# phonebook/admin.py
from django.contrib import admin
from .models import Contact

# Register models here
admin.site.register(Contact)
