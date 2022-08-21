from django.contrib import admin
from .models import Category, Project_info

@admin.register(Project_info)
class adminproject(admin.ModelAdmin):
    list_display = ('category', 'client', 'project_url','project_date')

admin.site.register(Category)

