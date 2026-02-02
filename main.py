from pprint import pprint

def get_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            if not dish_name:
                continue

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                raw_ingredient = file.readline().strip().split(' | ')
                name, qty, measure = raw_ingredient

                ingredients.append({
                    'ingredient_name': name,
                    'quantity' : int(qty),
                    'measure' : measure
                })

            cook_book[dish_name] = ingredients
            file.readline()

cook_book = get_cook_book('recipes.txt')
pprint(cook_book, sort_dicts=False, width=100)


