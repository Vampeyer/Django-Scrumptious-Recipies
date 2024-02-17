from turtle import title
from django.shortcuts import render, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def details(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {'recipe_object': recipe}
    return render(request, 'recipes/details.html', context)
def list(request):
    recipes = Recipe.objects.all()
    context = {
        "list": recipes,
    }
    return render(request, "recipes/recipes_list.html", context)

def create_post(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            form.save()
            return redirect('recipes_list')
    else:
        form = RecipeForm()

    context={ 'form': form,}
    return render(request, 'recipes/create.html', context)


#def edi_post(request, details_id):
#    detail = Recipe.objects.get(pk=details_id)
#    details = Recipe.objects.all()
#    if request.method == 'POST':
#        detail.save()
#        return redirect('/recipes/')
#    else:
#        return redirect('/recipes/')

def edit_post(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance = recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes_list')
    else:
        form = RecipeForm(instance = recipe)

    context={ 'form': form, 'recipe': recipe}
    return render(request, 'recipes/edit.html', context)

def my_recipe_list(request):
    
    recipes = Recipe.objects.filter(author=request.user)
    context = {
        "list": recipes,
    }
    return render(request, "recipes/recipes_list.html", context)





def my_recipe_list_id(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {
        "my_recipe_list_id": my_recipe_list_id,
    }
    return render(request, "recipes/recipes_list.html", context)
