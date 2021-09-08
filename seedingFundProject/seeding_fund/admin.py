from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectModel(admin.ModelAdmin):
    list_filter = ('name', 'description','sector')
    list_display = ('name', 'description','sector')
