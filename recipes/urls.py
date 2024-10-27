from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from .views import (GetCategoryView, GetRecipeByCategoryView,
                    GetRecipeByIdView, GetRecipeByNameView, GetRecipesView,
                    RecipeUpdateView, RegisterRecipeView,
                    SeedCategoriesAndRecipesView)

urlpatterns = [
    path('create/', RegisterRecipeView.as_view(), name='register'),
    path('list/', GetRecipesView.as_view(), name='get-recipes'),
    path('recipe/id/<int:id>/', GetRecipeByIdView.as_view(), name='get-recipe-by-id'),
    path('recipe/name/<str:title>/', GetRecipeByNameView.as_view(), name='get-recipe-by-name'),
    path('edit/<int:id>/', RecipeUpdateView.as_view(), name='update-recipe'),
    path('category/', GetCategoryView.as_view(), name='get-categories'),
    path('category/<int:category_id>/', GetRecipeByCategoryView.as_view(), name='get-recipe-by-category'),
    path('seed/', SeedCategoriesAndRecipesView.as_view(), name='seed-categories-recipes'),
]