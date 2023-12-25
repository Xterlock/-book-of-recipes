from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models


@admin.register(models.Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('title', 'description', 'ingredients', 'user',)
    search_fields = ('title',)


@admin.register(models.Category)
class RecipeAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
