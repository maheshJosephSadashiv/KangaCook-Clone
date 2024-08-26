from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_recipe, name='add_recipe'),
    path('list/', views.list_recipes, name='list_recipes'),
    path('favorite/<str:recipe_id>/', views.mark_favorite, name='mark_favorite'),
    path('favorites/', views.list_favorite_recipes, name='list_favorite_recipes'),
]