from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .domain.recipe_response import RecipeResponse
from .models import Recipe
import json


@csrf_exempt
def add_recipe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recipe = Recipe.objects.create(
            title=data['title'],
            ingredients=json.dumps(data['ingredients']),
            instructions=json.dumps(data['instructions']),
            cuisine=data['cuisine'],
            image_url=data['image_url'],
        )
        return JsonResponse({'message': 'Recipe added successfully', 'id': str(recipe.id)})


def list_recipes(request):
    recipes = Recipe.objects.all()
    recipe_list = []
    for recipe in recipes:
        recipe_list.append(RecipeResponse(recipe).__dict__())
    return JsonResponse({'recipes': recipe_list})


@csrf_exempt
def mark_favorite(request, recipe_id):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        recipe = Recipe.objects.get(id=recipe_id)
        recipe.is_favorite = body_data.get('is_favorite')
        recipe.save()
        return JsonResponse({'message': 'Recipe marked as favorite'})


def list_favorite_recipes(request):
    favorite_recipes = Recipe.objects.filter(is_favorite=True)
    recipe_list = []
    for recipe in favorite_recipes:
        recipe_list.append(RecipeResponse(recipe).__dict__())
    return JsonResponse({'recipes': recipe_list})
