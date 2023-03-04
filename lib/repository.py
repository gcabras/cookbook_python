import csv
from recipe import Recipe

class Repository:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.recipes = []
        self.load_csv()

    def all(self):
        self.load_csv
        return self.recipes

    def create(self, recipe):
        self.recipes.append(recipe)
        self.save_csv()

    def destroy(self, index):
        self.recipes.pop(index)
        self.save_csv()

    def load_csv(self):
        with open(self.csv_file_path) as csv_file:
            csv_rows = csv.reader(csv_file)
            for row in csv_rows:
                recipe = Recipe(row[0], row[1])
                self.recipes.append(recipe)

    def save_csv(self):
        with open(self.csv_file_path, "w") as csv_file:
            csv_rows = csv.writer(csv_file)
            for recipe in self.recipes:
                csv_rows.writerow([recipe.name, recipe.description])
