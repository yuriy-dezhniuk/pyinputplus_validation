from typing import List, Dict, Union

import pyinputplus as pyip


def select_ingredients(
        ingredients_menu: Dict[str, Dict[str, Union[float, int]]],
        optional_ingredients: List[str, ]
) -> List[str, ]:
    """
    Selects ingredients from the menu (ingredients_menu).

    Args:
        ingredients_menu (Dict): Ingredients menu with prices.
            {
                ingredient1(str): {
                    ingredient_type1(str): price(int or float),
                    ingredient_type2(str): price(int or float),
                },
                ingredient2(str): {
                    ingredient_type1(str): price(int or float),
                    ingredient_type2(str): price(int or float),
                },
                ...
            }
        optional_ingredients (List): List of optional ingredients
            [ingredient1(str), ingredient2(str), ...]

    Returns:
        List: List of ingredients selected by the user.
            [ingredient1(str), ingredient2(str), ...]
    """
    ordered_ingredients = []  # ingredients selected by the user

    for ingredient_type in ingredients_menu.keys():
        # Check that customer wants to add an optional ingredient
        if ingredient_type in optional_ingredients:
            add_ingredient = True if pyip.inputYesNo(prompt=f'Do you want {ingredient_type}?\n') == 'yes' else False
            if not add_ingredient:
                continue
        # Select type of ingredient
        ingredient = pyip.inputMenu(
            list(ingredients_menu[ingredient_type].keys()),
            prompt=f'What type of {ingredient_type} would you like ?\n',
            blank=True
        )
        ordered_ingredients.append(ingredient)  # Add selected type of ingredient to the sandwiches

    return ordered_ingredients

