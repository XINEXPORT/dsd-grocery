# Generated by Django 4.2.11 on 2024-04-15 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DietaryPreferences",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("preference_name", models.CharField(max_length=100)),
                ("is_selected", models.BooleanField(default=False)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preferences",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FavoriteRecipes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("servings", models.IntegerField()),
                (
                    "preference_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.dietarypreferences",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorite_recipes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ingredients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity_available",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "preference_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.dietarypreferences",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredients",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShoppingList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_purchased", models.BooleanField(default=False)),
                (
                    "ingredient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.ingredients",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shopping_list",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Macros",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("macro_type", models.CharField(max_length=50)),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "ingredient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.ingredients",
                    ),
                ),
                (
                    "recipe_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.favoriterecipes",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="macros",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
