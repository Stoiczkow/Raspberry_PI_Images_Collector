from django.contrib import admin
from .models import ScreenShots, Files
# Register your models here.


@admin.register(ScreenShots)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Files)
class AuthorAdmin(admin.ModelAdmin):
    pass