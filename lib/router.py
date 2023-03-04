class Router:
    def __init__(self, controller):
        self.controller = controller
        self.running = True

    def run(self):
        while self.running:
            print("Welcome to the PyCookbook 🐍")
            print("What do you like to do?")
            self.display_actions()
            action = int(input(""))
            if action == 1:
                self.controller.list()
            elif action == 2:
                self.controller.add()
            elif action == 3:
                self.controller.remove()
            elif action == 4:
                self.stop()

    def display_actions(self):
        print("1 - List all the recipes")
        print("2 - Add a recipe")
        print("3 - Remove a recipe")
        print("4 - Exit")

    def stop(self):
        self.running = False
