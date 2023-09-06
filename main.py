import pyinputplus as pyip

from sandwiches_menu import ingredients_menu, optional_ingredients
from select_ingredients import select_ingredients


ordered_ingredients = select_ingredients(ingredients_menu, optional_ingredients)  # ingredients selected by the user

# Calculation of the cost of one sandwich
one_sandwich_price = 0
for ingredient_type in ingredients_menu.keys():
    for ingredient in ingredients_menu[ingredient_type].keys():
        if ingredient in ordered_ingredients:
            one_sandwich_price += ingredients_menu[ingredient_type][ingredient]


amount_of_sandwiches = pyip.inputInt(prompt='How many sandwiches do you want?\n')
total_price = one_sandwich_price * amount_of_sandwiches
print('ordered_ingredients', ordered_ingredients)
print('amount_of_sandwiches', amount_of_sandwiches)
print('total_price', total_price)


# TODO: Create a "make_an_order" function and move it to separate file
# TODO: Create a "cost_of_sandwich" function and move it to separate file
# TODO: Create a "total_price" function and move it to separate file
