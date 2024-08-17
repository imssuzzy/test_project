from django.contrib import admin
from .models import Category, Property

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name',)