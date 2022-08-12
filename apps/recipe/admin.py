from django.contrib import admin

from .models import Category, Recipe, RecipeStatistic, RecipeIngredient


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientAdmin]
    list_display = ['name', 'created']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Recipe


@admin.register(RecipeStatistic)
class ArticleStatisticAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'date', 'views')
    search_fields = ('recipe_name', )


