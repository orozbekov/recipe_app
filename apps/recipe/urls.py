from django.urls import path

from .views import CategoryListCreateAPIView, RecipeListCreateAPIView, \
    CategoryDetailAPIView, about, contact, RecipeDetailView, RecipesListSearchView, tag_template, tags, error_404, \
    RecipeListView

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('recipe/<slug:slug>/', RecipeDetailView.as_view(), name='single-recipe'),
    path('recipes/', RecipesListSearchView.as_view(), name='recipes'),
    path('category/', tags, name='tags'),
    path('tag-template/', tag_template, name='tag-template'),
    path('error_404/', error_404, name='error_404'),
    path('api/v1/category/', CategoryListCreateAPIView.as_view()),
    path('api/v1/category/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('api/v1/recipe/', RecipeListCreateAPIView.as_view()),
]