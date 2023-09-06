import pyinputplus as pyip

from sandwiches_menu import ingredients_price, optional_ingredients


ordered_ingredients = []

# Select ingredients
for ingredient_type in ingredients_price.keys():
    # Check that customer wants to add an optional ingredient
    if ingredient_type in optional_ingredients:
        add_ingredient = True if pyip.inputYesNo(prompt=f'Do you want {ingredient_type}?\n') == 'yes' else False
        if not add_ingredient:
            continue
    # Select type of ingredient
    ingredient = pyip.inputMenu(
        list(ingredients_price[ingredient_type].keys()),
        prompt=f'What type of {ingredient_type} would you like ?\n',
        blank=True
    )
    ordered_ingredients.append(ingredient)  # Add selected type of ingredient to the sandwiches

# Calculation of the cost of one sandwich
one_sandwich_price = 0
for ingredient_type in ingredients_price.keys():
    for ingredient in ingredients_price[ingredient_type].keys():
        if ingredient in ordered_ingredients:
            one_sandwich_price += ingredients_price[ingredient_type][ingredient]


amount_of_sandwiches = pyip.inputInt(prompt='How many sandwiches do you want?\n')
total_price = one_sandwich_price * amount_of_sandwiches
print('ordered_ingredients', ordered_ingredients)
print('amount_of_sandwiches', amount_of_sandwiches)
print('total_price', total_price)


# TODO: Create a "make_an_order" function and move it to separate file
# TODO: Create a "cost_of_sandwich" function and move it to separate file
# TODO: Create a "total_price" function and move it to separate file
