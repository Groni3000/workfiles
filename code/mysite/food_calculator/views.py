from django.shortcuts import render
from .models import FoodProduct
from .forms import food_info
from .services import func_name_of_tables

# Create your views here.
def evaluate(request):
    #FoodProduct fields:
    # prod_name
    # prod_type
    # prod_calories
    # prod_proteins
    # prod_fats
    # prod_carbohydrates
    # el_of_tables, name_of_tables = content_of_tables() MAYBE WILL USE, but no, actually
    if request.method=="GET":
        products=FoodProduct.food.all()
        len_of_prods=[i for i in range(len(products))]
        name_of_tables = func_name_of_tables(products)
        form=food_info()
        context={
            'len_of_prods': len_of_prods,
            'products': products,
            'name_of_tables': name_of_tables,
            'form': form
        }
        return render(request, 'food_calculator/evaluate.html', context)
    else:
        products=FoodProduct.food.all()
        len_of_prods=[i for i in range(len(products))]
        name_of_tables = func_name_of_tables(products)
        form=food_info(request.POST)
        a=form['food_form'][0].data['value'].split(',')
        f=[]
        for el in a:
           for product in products:
              if el==product.prod_name:
                  f.append(product)
                  break
        #f=[selected_product1,...,selected_productk]
        list_of_names_of_selected_products=[el.prod_name for el in f]
        list_of_calories_of_selected_products=[el.prod_calories for el in f]
        list_of_proteins_of_selected_products=[el.prod_proteins for el in f]
        list_of_fats_of_selected_products=[el.prod_fats for el in f]
        list_of_carbohydrates_of_selected_products=[el.prod_carbohydrates for el in f]
        sum_of_calories_of_selected_products=sum(list_of_calories_of_selected_products)
        sum_of_proteins_of_selected_products=sum(list_of_proteins_of_selected_products)
        sum_of_fats_of_selected_products=sum(list_of_fats_of_selected_products)
        sum_of_carbohydrates_of_selected_products=sum(list_of_carbohydrates_of_selected_products)
        context={
            'len_of_prods': len_of_prods,
            'products': products,
            'name_of_tables': name_of_tables,
            'list_of_selected_products': f,
            'list_of_names_of_selected_products': list_of_names_of_selected_products,
            'sum_of_calories_of_selected_products': sum_of_calories_of_selected_products,
            'sum_of_proteins_of_selected_products': sum_of_proteins_of_selected_products,
            'sum_of_fats_of_selected_products': sum_of_fats_of_selected_products,
            'sum_of_carbohydrates_of_selected_products': sum_of_carbohydrates_of_selected_products
        }
        return render(request, 'food_calculator/evaluate.html', context)




