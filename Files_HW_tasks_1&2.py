import os

recipes = os.path.join(os.getcwd(), 'recipes.txt')

with open(recipes, 'r', encoding='utf-8') as recipes_file:
    cook_book = {}
    for d in recipes_file:
        dish_name = d.strip()
        person_quantity = int(recipes_file.readline())
        ingridients = []
        for x in range(person_quantity):
            ingrd = recipes_file.readline().strip().split(' | ')
            ing_name, ing_quantity, ing_measure = ingrd
            ingridients.append({'ingredient_name': ing_name,
                                'quantity': int(ing_quantity),
                                'measure': ing_measure})
        recipes_file.readline()
        cook_book.setdefault(dish_name, ingridients)


    def get_shop_list_by_dishes(dishes, person_quantity):
        shop_list = {}
        for dish_name in dishes:
            if dish_name in cook_book:
                for ingreds in cook_book[dish_name]:
                    ing_quantity = {}
                    # total_quant = 0
                    if ingreds['ingredient_name'] not in shop_list:
                        ing_quantity['measure'] = ingreds['measure']
                        ing_quantity['quantity'] = ingreds['quantity'] * person_quantity
                        shop_list[ingreds['ingredient_name']] = ing_quantity
                    else:
                        shop_list[ingreds['ingredient_name']]['quantity'] = \
                            shop_list[ingreds['ingredient_name']]['quantity'] + ingreds['quantity'] * person_quantity
            else:
                return (f'Блюда {dish_name} нет в кулинарной книге')

        return shop_list



