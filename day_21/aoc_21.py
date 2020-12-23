import re
import sys

input_data_filename = "food_data.txt"
# input_data_filename = "food_data_short.txt"

all_allergens = set()
all_ingredients = set()
foods = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        match = re.search("(.+) \(contains (.+)\)", line)
        if match:
            ingredients_str = match.group(1)
            ingredients = set(ingredients_str.split())
            allergens_str = match.group(2)
            allergens = set(allergens_str.split(", "))
            # print(f"ingredients_str={ingredients_str}")
            # print(f"ingredients={ingredients}")
            # print(f"allergens_str={allergens_str}")
            # print(f"allergens={allergens}")
            foods.append([ingredients, allergens])
            all_allergens |= allergens
            all_ingredients |= ingredients
print(f"foods={foods}")
print(f"all_allergens={all_allergens}")
print(f"all_ingredients={all_ingredients}")

allergen_ingredient_assoc = {}
allergic_ingredients = set()
foods_work = foods.copy()
while len(all_allergens) > 0:
    solved_allergen = None
    for allergen in list(all_allergens):
        sets = []
        for food in foods_work:
            if allergen in food[1]:
                sets.append(food[0])
        common_ingredients = set.intersection(*sets)
        # print(f"common_ingredients={common_ingredients}")
        if len(common_ingredients) == 1:
            solved_allergen = allergen
            allergic_ingredient = list(common_ingredients)[0]
            # print(f"solved_allergen={solved_allergen}")
            allergen_ingredient_assoc[solved_allergen] = allergic_ingredient
            allergic_ingredients |= {allergic_ingredient}
            for food in foods_work:
                food[0] -= common_ingredients
            break
    if solved_allergen is not None:
        all_allergens.remove(solved_allergen)
print(f"allergen_ingredient_assoc={allergen_ingredient_assoc}")
print(f"allergic_ingredients={allergic_ingredients}")

appearances = 0
for food in foods:
    for ingredient in food[0]:
        if ingredient not in allergic_ingredients:
            appearances += 1
print(f"appearances={appearances}")

