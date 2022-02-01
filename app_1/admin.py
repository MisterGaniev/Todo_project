from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import ToDo

# Register your models here.

@admin.register(ToDo)
class ToDo_admin(ModelAdmin):
    search_fields = ['id', 'title']
    list_filter = ['status']
    ordering = ['time']
    list_display = ['title','description', 'status']


