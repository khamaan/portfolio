from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email', "ip_address"]

admin.site.register(Contact,ContactAdmin)