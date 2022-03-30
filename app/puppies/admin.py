from django.contrib import admin
from .models import Puppy

@admin.register(Puppy)
class PuppyAdmin(admin.ModelAdmin):
    pass