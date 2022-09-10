from django.shortcuts import redirect
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'burgerplace/index.html'

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context["ingredients"] = Ingredient.objects.all()
    #     context["menuitems"] = MenuItem.objects.all()
    #     # context["reciperequirements"] = RecipeRequirement.objects.all()
    #     return context

class IngredientsView(ListView):
    model = Ingredient
    template_name = 'burgerplace/ingredients.html'

class CreateIngredientView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'burgerplace/create_ingredient.html'

class MenuItemsView(ListView):
    model = MenuItem
    template_name = 'burgerplace/menuitems.html'

class CreateMenuItemView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'burgerplace/create_menuitem.html'

class RecipesRequirementsView(TemplateView):
    template_name = 'burgerplace/reciperequirements.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItem.objects.filter(id=kwargs['menuitem']).first()
        context["reciperequirements"] = RecipeRequirement.objects.filter(menuitem=kwargs['menuitem'])
        if len(context["reciperequirements"]) == 0:
            context["reciperequirements"] = [{'quantity':0, 'ingredient':'No ingredients found'}]
        return context

class CreateRecipeRequirementView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'burgerplace/create_reciperequirement.html'

class PurchasesView(ListView):
    model = Purchase
    template_name = 'burgerplace/purchases.html'

class CreatePurchaseView(TemplateView):
    template_name = 'burgerplace/create_purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menuitems"] = MenuItem.objects.all()
        return context

    def post(self, request):
        menuitem_id = request.POST["menuitem"]
        menuitem = MenuItem.objects.get(pk=menuitem_id)
        requirements = RecipeRequirement.objects.filter(menuitem=menuitem)
        purchase = Purchase(menuitem=menuitem)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_quantity = requirement.quantity
            ingredient_item = Ingredient.objects.get(pk=required_ingredient.id)
            ingredient_item.available_quantity -= required_quantity
            ingredient_item.save()

        purchase.save()
        return redirect("/purchases")