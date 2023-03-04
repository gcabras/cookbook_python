class View:
    def display_recipes(self, recipe_list):
        for index in range(0, len(recipe_list) - 1):
            print(str(index + 1) + " - " + recipe_list[index].name)

    def ask_user_for(self, user_input):
        output = input("Which is the {input}?\n".format(input=user_input))
        return output
