from django.conf import settings
from django.db import models


class DietaryPreference(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="dietary_preferences_entries",
    )
    preference_name = models.CharField(max_length=100)
    is_selected = models.BooleanField(default=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preference = models.ForeignKey(
        DietaryPreference, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.name} ({self.quantity})"


class ShoppingList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    is_purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ingredient.name} ({self.quantity})"


class FavoriteRecipe(models.Model):
    servings = models.IntegerField()
    preference = models.ForeignKey(
        DietaryPreference, on_delete=models.CASCADE, related_name="favorite_recipes"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="favorite_recipes",
    )
    name = models.CharField(max_length=100, default=False)
    image = models.CharField(max_length=255, default=False)
    minutes = models.CharField(max_length=100, default=False)
    likes = models.CharField(max_length=100, default=False)

    def __str__(self):
        return self.name


class Macro(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(FavoriteRecipe, on_delete=models.CASCADE)
    macro_type = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.recipe.name} ({self.quantity})"


class PlannedRecipe(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="planned_recipes",
    )
    date_for = models.DateField()
    recipe = models.ForeignKey(FavoriteRecipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe.name} on {self.date_for}"
