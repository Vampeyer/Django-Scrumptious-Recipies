from django.db import models
from django.conf import settings


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='recipes',
        on_delete=models.CASCADE,
        null=True,
    )

class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

class RecipeStep(models.Model):
    instruction = models.TextField()
    order = models.PositiveIntegerField()
    recipe = models.ForeignKey(
        'Recipe',
        related_name='steps',
        on_delete=models.CASCADE,
    )
    def recipe_title(self):
        return self.recipe.title
    class Meta:
        ordering = ['order']


class RecipeIngredients(models.Model):
    food_item = models.TextField()
    amount = models.TextField()
    recipe = models.ForeignKey(
        'Recipe',
        related_name='ingredients',
        on_delete=models.CASCADE,
    )
    def recipe_title(self):
        return self.recipe.title
    class Meta:
        ordering = ['food_item']




# Create your models here.
