import json


class RecipeResponse:
    def __init__(self, db_recipe):
        self.id = db_recipe.id
        self.title = db_recipe.title
        self.ingredients = json.loads(db_recipe.ingredients)
        self.instructions = json.loads(db_recipe.instructions)
        self.image_url = db_recipe.image_url
        self.cuisine = db_recipe.cuisine
        self.is_favorite = db_recipe.is_favorite

    def __dict__(self):
        # Convert the object to a dictionary
        return {
            "id": self.id,
            'title': self.title,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'image_url': self.image_url,
            'cuisine': self.cuisine,
            'is_favorite': self.is_favorite,
        }
