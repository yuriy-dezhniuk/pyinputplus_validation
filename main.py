import pyinputplus as pyip

from sandwiches_menu import ingredients_menu, optional_ingredients
from select_ingredients import select_ingredients
from sandwich_cost_calculation import sandwich_cost_calculation


ordered_ingredients = select_ingredients(ingredients_menu, optional_ingredients)  # ingredients selected by the user

one_sandwich_price = sandwich_cost_calculation(ingredients_menu, ordered_ingredients)  # Cost of one sandwich

# Amount of sandwiches the user wants to buy.
amount_of_sandwiches = pyip.inputInt(prompt='How many sandwiches do you want?\n')

total_cost = one_sandwich_price * amount_of_sandwiches
print('ordered_ingredients', ordered_ingredients)
print('amount_of_sandwiches', amount_of_sandwiches)
print('total_price', total_cost)
