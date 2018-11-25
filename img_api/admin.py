from django.contrib import admin
from .models import ScreenShots
# Register your models here.


@admin.register(ScreenShots)
class AuthorAdmin(admin.ModelAdmin):
    pass