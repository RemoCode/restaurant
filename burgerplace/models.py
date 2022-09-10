from django.db import models

class Ingredient(models.Model):
    name = models.CharField(unique=True, max_length=200)
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    available_quantity = models.IntegerField(default=0)

    def get_absolute_url(self): # define where to send user after submitting form
        return "/ingredients"

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    name = models.CharField(unique=True, max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return "/menuitems"

    def __str__(self):
        return f"{self.name}"

class RecipeRequirement(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return f"{'/reciperequirements/'}{self.menuitem.id}"

    def __str__(self):
        return f"{self.menuitem}{': '}{self.quantity}{'x '}{self.ingredient}"

class Purchase(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    datetime_of_purchase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menuitem}"