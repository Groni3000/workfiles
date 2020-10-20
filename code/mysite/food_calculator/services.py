from .models import FoodProduct


#TODO
'''Need to think about this very ... non-reuseable function'''
def content_of_tables():
    options=FoodProduct.food.values_list('prod_name','prod_type')
    k=options[0][1]
    products=[[[k]]]
    j=0
    for i in range(len(options)):
        if options[i][1]==k:
            products[j].append(options[i][0])
        else:
            k=options[i][1]
            products.append([[k]])
            j=j+1
            products[j].append(options[i][0])

    #Так меняется таблица
    # print(products[0][0][0])
    # print(products[1][0][0])
    # Так меняются продукты
    # print(products[0][1])
    # print(products[0][2])

    name_of_tables=[products[i][0][0] for i in range(len(products))]
    el_of_tables={
        name_of_tables[k]:[products[k][i] for i in range(1,len(products[k]))]
        for k in range(len(products))
    }
    return el_of_tables, name_of_tables


def func_name_of_tables(products):
    name_of_tables=[]
    for product in products:
        if product.prod_type not in name_of_tables:
            name_of_tables.append(product.prod_type)
    return name_of_tables

def func_get_list_of_selected_products(form, products):
    a=form['food_form'][0].data['value'].split(',') #List of selected prod_names
    f=[] #It will be list of selected products (thus, I can access attributes: prod_name, prod_calories, etc...)
    for el in a:
       for product in products:
          if el==product.prod_name:
              f.append(product)
              break
    return f