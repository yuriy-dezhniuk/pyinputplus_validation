from typing import List, Dict, Union


def sandwich_cost_calculation(
        ingredients_menu: Dict[str, Dict[str, Union[float, int]]],
        ordered_ingredients: List[str],
) -> Union[float, int]:
    """
    Calculation of the cost of one sandwich based on ingredients selected by the customer

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
        ordered_ingredients (List): List of ordered ingredients
            [ingredient1(str), ingredient2(str), ...]

    Returns:
        int or float: cost of one sandwich.
    """
    sandwich_price = 0
    for ingredient_type in ingredients_menu.keys():
        for ingredient in ingredients_menu[ingredient_type].keys():
            if ingredient in ordered_ingredients:
                sandwich_price += ingredients_menu[ingredient_type][ingredient]
    return sandwich_price
