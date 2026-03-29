def is_available_to_order_set(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True

shop_menus = ['만두','떡볶이','오뎅','사이다','콜라']
shop_orders = ['오뎅','콜라','만두','환타']

print(is_available_to_order_set(shop_menus,shop_orders))