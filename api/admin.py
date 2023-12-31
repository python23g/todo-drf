from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'completed', 'created']
    list_filter = ['completed', 'created']
    search_fields = ['title', 'description']
    ordering = ['title', 'completed', 'created']
    list_per_page = 10
