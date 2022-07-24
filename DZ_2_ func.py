cook_book = {
  'Омлет': [
    {'ingredient_name': 'Картофель', 'quantity': 5, 'measure': 'кг'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for items in dishes:
        if items not in cook_book:
            print(f'Блюдо {items} отсутствует')

        for keys, values in cook_book.items():
             if keys in items:
                 for value in values:
                     a = value.pop('ingredient_name')
                     if a not in shop_list.keys():
                         value['quantity'] *= person_count
                         shop_list[a] = value
                     else:
                         shop_list[a]['quantity'] += value['quantity'] * person_count
    return shop_list

print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 1))