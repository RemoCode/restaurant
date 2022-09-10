from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('logout/', views.log_out, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('ingredients/create/', views.CreateIngredientView.as_view(), name='create_ingredient'),
    path('menuitems/', views.MenuItemsView.as_view(), name='menuitems'),
    path('menuitems/create/', views.CreateMenuItemView.as_view(), name='create_menuitem'),
    path('reciperequirements/<menuitem>', views.RecipesRequirementsView.as_view(), name='reciperequirements'),
    path('reciperequirements/create/', views.CreateRecipeRequirementView.as_view(), name='create_reciperequirement'),
    path('purchases/', views.PurchasesView.as_view(), name='purchases'),
    path('purchases/create/', views.CreatePurchaseView.as_view(), name='create_purchase')
]