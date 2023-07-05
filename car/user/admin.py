from django.contrib import admin

from .models import User


# Registering User Model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
