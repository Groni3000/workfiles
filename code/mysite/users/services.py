


def prepared_results(user_product_menus):
    user_results=[[user_product_menus[i]] for i in range(len(user_product_menus))]
    for i in range(len(user_results)):
        user_monday_products_for_menu=[user_product_menus[i].list_of_selected_products_monday.all() for i in range(len(user_product_menus))]
        user_tuesday_products_for_menu=[user_product_menus[i].list_of_selected_products_tuesday.all() for i in range(len(user_product_menus))]
        user_wednesday_products_for_menu=[user_product_menus[i].list_of_selected_products_wednesday.all() for i in range(len(user_product_menus))]
        user_thursday_products_for_menu=[user_product_menus[i].list_of_selected_products_thursday.all() for i in range(len(user_product_menus))]
        user_friday_products_for_menu=[user_product_menus[i].list_of_selected_products_friday.all() for i in range(len(user_product_menus))]
        user_saturday_products_for_menu=[user_product_menus[i].list_of_selected_products_saturday.all() for i in range(len(user_product_menus))]
        user_sunday_products_for_menu=[user_product_menus[i].list_of_selected_products_sunday.all() for i in range(len(user_product_menus))]

        user_results[i].append(['monday', user_monday_products_for_menu[i]])
        user_results[i].append(['tuesday', user_tuesday_products_for_menu[i]])
        user_results[i].append(['wednesday', user_wednesday_products_for_menu[i]])
        user_results[i].append(['thursday', user_thursday_products_for_menu[i]])
        user_results[i].append(['friday', user_friday_products_for_menu[i]])
        user_results[i].append(['saturday', user_saturday_products_for_menu[i]])
        user_results[i].append(['sunday', user_sunday_products_for_menu[i]])
    return user_results