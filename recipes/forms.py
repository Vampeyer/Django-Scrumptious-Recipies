from django.forms import ModelForm
from recipes.models import Recipe


class RecipeForm(ModelForm):    # Step 1
    class Meta:                 # Step 2
        model = Recipe          # Step 3
        fields = [              # Step 4
            "title",            # Step 4
            "picture",          # Step 4
            "description",      # Step 4
        ]
class RecipeSteps(ModelForm):pass
