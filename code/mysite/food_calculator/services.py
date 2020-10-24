from .models import FoodProduct


#TODO
'''Need to think about this very ... non-reuseable function'''
def content_of_tables():
    products=FoodProduct.food.all()
    name_of_tables=[]
    for product in products:
        if product.prod_type in name_of_tables:
            pass
        else:
            name_of_tables.append(product.prod_type)

    list_of_choices=[
        [name_of_tables[i],
        [
            [product,product] for product in products if product.prod_type==name_of_tables[i]
        ] 
        ] for i in range(len(name_of_tables))
        ]
    #making it tuple (but it's not required i think)
    for i in range(len(list_of_choices)):
        for j in range(len(list_of_choices[i][1])):
            list_of_choices[i][1][j]=tuple(list_of_choices[i][1][j])
        list_of_choices[i][1]=tuple(list_of_choices[i][1])
        list_of_choices[i]=tuple(list_of_choices[i])

    return list_of_choices


def make_list_of_selected_products(selected_product_names_list):
    all_products=FoodProduct.food.all()
    result=[]
    for el in selected_product_names_list:
        for product in all_products:
            if el==product.prod_name:
                result.append(product)
                break
    return result


    