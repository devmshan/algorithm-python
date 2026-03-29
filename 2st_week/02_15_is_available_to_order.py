def is_available_to_order(menus, value):
    max_menus = len(menus) - 1
    min_menus = 0
    guess = (min_menus + max_menus) // 2

    while min_menus <= max_menus:
        if menus[guess] == value:
            return True
        elif menus[guess] > value:
            # 값이 더 작으므로 오른쪽 범위 축소
            max_menus = guess - 1
        else:
            # 값이 더 크므로 왼쪽 범위 축소
            min_menus = guess + 1
        guess = (min_menus + max_menus) // 2
    return False

def is_available_to_order_list(menus, orders):
    menus.sort()
    for i in range(len(orders)):
        if not is_available_to_order(menus, orders[i]):
            return False
    return True

shop_menus = ['만두','떡볶이','오뎅','사이다','콜라']
shop_orders = ['오뎅','콜라','만두','환타']

print(is_available_to_order_list(shop_menus,shop_orders))