def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                # Умножаем количество на число гостей
                quantity = ingredient['quantity'] * person_count

                if name not in shop_list:
                    # Если продукта еще нет в списке, добавляем его
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    # Если продукт уже есть, суммируем количество
                    shop_list[name]['quantity'] += quantity
