from django.urls import path
from .views import details, edit_post
from .views import list, create_post, edit_post,my_recipe_list

urlpatterns = [
    path('recipes/details/<int:id>', details, name = 'details'),
    path('recipes/', list, name = 'recipes_list'),
    path('recipes/create/', create_post, name = 'create_post'),
    path('recipes/details/<int:id>/edit/', edit_post, name = 'edits'),
    path("mine/", my_recipe_list, name="my_recipe_list"), 
    path("mine/details/<int:id>", details, name="my_recipe_list"),


]
