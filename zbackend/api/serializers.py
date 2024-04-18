from rest_framework import serializers
from .models import (
    FavoriteRecipes,
    DietaryPreferences,
    User,
    Ingredients,
    ShoppingList,
    Macros,
)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ["id", "quantity_available", "preference"]


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ["id", "user", "ingredient", "quantity", "is_purchased"]

        extra_kwargs = {"user": {"read_only": True}, "ingredient": {"required": True}}


class MacrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macros
        fields = ["id", "user", "recipe", "macro_type", "ingredient", "quantity"]


class FavoriteRecipeSerializer(serializers.ModelSerializer):
    preference = serializers.PrimaryKeyRelatedField(
        queryset=DietaryPreferences.objects.all()
    )
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = FavoriteRecipes
        fields = [
            "servings",
            "preference",
            "user",
            "id",
            "name",
            "image",
            "minutes",
            "likes",
        ]
