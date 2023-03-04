from view import View
from repository import Repository
from recipe import Recipe

class Controller:
    def __init__(self, repository):
        self.repository = repository
        self.view = View()

    def list(self):
        recipes = self.repository.all()
        self.view.display_recipes(recipes)

    def add(self):
        recipe_name = self.view.ask_user_for("recipe name")
        recipe_description = self.view.ask_user_for("recipe description")
        recipe = Recipe(recipe_name, recipe_description)
        self.repository.create(recipe)

    def remove(self):
        self.list()
        index_recipe = int(self.view.ask_user_for("index"))
        self.repository.destroy(index_recipe - 1)
