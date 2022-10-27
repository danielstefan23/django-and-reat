from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'specializare', 'grupa_sanguina', 'job')

admin.site.register(User, CustomUser)