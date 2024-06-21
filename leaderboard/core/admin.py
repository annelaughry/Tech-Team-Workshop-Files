from django.contrib import admin
from .models import Team

@admin.register(Team)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo')
    def display_logo(self, obj):
        return obj.logo.url if obj.logo else ''
    display_logo.short_description = 'Logo'