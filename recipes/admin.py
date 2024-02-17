from django.contrib import admin
from recipes.models import Recipe, RecipeStep, RecipeIngredients

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
    ]

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ('recipe_title',
                    'order',
                    'id')
@admin.register(RecipeIngredients)
class RecipeIngredients(admin.ModelAdmin):
    list_display = ('recipe_title',
                    'food_item',
                    'id')
# Register your models here.
