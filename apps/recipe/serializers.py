from rest_framework import serializers

from .models import Category, Recipe, RecipeIngredient, RecipeStatistic


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для категории.
    """
    
    class Meta:
        model = Category
        fields = ('id', 'title', 'image_url', 'description')


class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модельки еды.
    """
    ingredient = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'category_name', 'name', 'image_url', 'description',
                  'instructions', 'area', 'youtube_url', 'ingredient')


class RecipeStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStatistic
        fields = ('recipe', 'views', 'date')
