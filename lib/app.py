from repository import Repository
from controller import Controller
from router import Router

recipe_csv = "data/recipes.csv"
repo = Repository(recipe_csv)
controller = Controller(repo)
router = Router(controller)

router.run()
