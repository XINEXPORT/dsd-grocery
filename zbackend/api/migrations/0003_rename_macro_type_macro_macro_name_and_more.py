# Generated by Django 5.0.4 on 2024-04-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_dietarypreference_user_favoriterecipe_preference_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="macro",
            old_name="macro_type",
            new_name="macro_name",
        ),
        migrations.RenameField(
            model_name="macro",
            old_name="recipe",
            new_name="recipe_id",
        ),
        migrations.RemoveField(
            model_name="favoriterecipe",
            name="recipe",
        ),
        migrations.RemoveField(
            model_name="ingredient",
            name="preference",
        ),
        migrations.RemoveField(
            model_name="macro",
            name="ingredient",
        ),
        migrations.RemoveField(
            model_name="macro",
            name="name",
        ),
        migrations.RemoveField(
            model_name="plannedrecipe",
            name="recipe",
        ),
        migrations.RemoveField(
            model_name="shoppinglist",
            name="ingredient",
        ),
        migrations.AddField(
            model_name="favoriterecipe",
            name="recipe_id",
            field=models.CharField(default=157344, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="plannedrecipe",
            name="recipe_id",
            field=models.CharField(default=157344, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shoppinglist",
            name="product_id",
            field=models.CharField(default=12061, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="shoppinglist",
            name="image",
            field=models.CharField(
                default="https://placeholder.pics/svg/300/DEDEDE/555555/image",
                max_length=255,
            ),
        ),
    ]
