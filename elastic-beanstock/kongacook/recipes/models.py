from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.TextField()
    cuisine = models.TextField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
