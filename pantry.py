import random


class Food:
    instances = []

    def __init__(self, name: str, formatted_name: str, time: str, ingredients: list, difficulty: int):
        self.name = name
        self.formatted_name = formatted_name
        self.time = time
        self.ingredients = ingredients
        self.difficulty = difficulty
        __class__.instances.append(self)


# LIST OF MEALS:
LEEK_AND_MUSHROOM_PASTA = Food("leek_and_mushroom_pasta", "Leek and Mushroom Pasta", "lunch/dinner",
                               ["pasta", "mushrooms", "leeks", "cream", "pamersan"], 1)
COURGETTE_AND_CARROT_CAKES = Food("courgette_and_carrot_cakes", "Courgette and Carrot Cakes", "lunch/dinner",
                                  ["courgette", "carrots", "breadcrumbs", "feta cheese"], 2)
CIBATTA_BREAD_WITH_RICOTTA = Food("cibatta_bread_with_ricotta", "Cibatta Bread with Ricotta", "lunch",
                                  ["cibatta bread", "ricotta", "tomato", "onion", "courgette", "italian spice"], 1)
VEGETABLE_SOUP = Food("vegetable_soup", "Vegetable Soup", "lunch/dinner", ["carrots", "onions", ], 2)
MUSTARD_MASH = Food("mustard_mash", "Mustard Mash", "dinner",
                    ["dijon mustard", "wholegrain mustard", "potatoes", "cream"], 1)
POTATO_CURRY = Food("potato_curry", "Potato Curry", "dinner", ["potatoes", "curry powder", "cream",
                                                               "tomatoes", "onions", "garlic", "four spice", "paprika",
                                                               "ginger"], 2)
SALMON_PASTA = Food("salmon_pasta", "Salmon Pasta", "dinner",
                    ["salmon", "pasta", "cream", "onions", "nutmeg", "butter"], 1)
RISOTTO = Food("risotto", "Risotto", "dinner", ["risotto", "leeks", "cream", "pamersan", "paprika"], 2)
MASH_POTATOES = Food("mash_potatoes", "Mash Potatoes", "dinner", ["potatoes", "comte", "butter", "milk"], 1)
ROLLS = Food("rolls", "Rolls", "lunch", ["oven rolls", "wildcard"], 1)
SALAD = Food("salad", "Salad", "lunch", ["salad", "cheese", "tomatoes", "croutons", "wildcard"], 1)
WRAPS = Food("wraps", "Wraps", "lunch/dinner", ["wraps", "wildcard"], 1)
PORRIDGE = Food("porridge", "Porridge", "breakfast", ["oats", "milk", "maple syrup"], 1)
PANCAKES = Food("pancakes", "Pancakes", "breakfast", ["butter", "milk", "maple syrup", "yeast"], 2)

# LIST OF SIDES:


def get_random_food():
    rand_index = random.randrange(len(Food.instances))
    rand_food = Food.instances[rand_index]
    rand_ingredients = ", ".join(rand_food.ingredients)
    print(rand_food.formatted_name)
    print(f"You will need: {rand_ingredients}")


def get_breakfast(days):
    i = 0
    while i != days:
        rand_index = random.randrange(len(Food.instances))
        rand_food = Food.instances[rand_index]
        if rand_food.time == "breakfast":
            rand_ingredients = ", ".join(rand_food.ingredients)
            print(rand_food.formatted_name)
            print(f"You will need: {rand_ingredients}")
            i = i + 1


def get_lunch(days):
    i = 0
    while i != days:
        rand_index = random.randrange(len(Food.instances))
        rand_food = Food.instances[rand_index]
        if "lunch" in rand_food.time:
            rand_ingredients = ", ".join(rand_food.ingredients)
            print(rand_food.formatted_name)
            print(f"You will need: {rand_ingredients}")
            i = i + 1


def get_dinner(days):
    i = 0
    while i != days:
        rand_index = random.randrange(len(Food.instances))
        rand_food = Food.instances[rand_index]
        if "dinner" in rand_food.time:
            rand_ingredients = ", ".join(rand_food.ingredients)
            print(rand_food.formatted_name)
            print(f"You will need: {rand_ingredients}")
            i = i + 1


print(Food.instances)
get_breakfast(3)
get_lunch(3)
get_dinner(4)
