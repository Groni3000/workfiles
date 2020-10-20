from django.shortcuts import render
from .models import FoodProduct
from .forms import food_info
from .services import func_name_of_tables, func_get_list_of_selected_products

# Create your views here.
def evaluate(request):
        # PLANS:
        # - Make a form that can add chosen products (probably in GET method) to menu for certain day and part of that day.
        # - Make a 'progress bar' for autheticated users (using his values: height, weight, age and something else?) that accumulates all values of
        # calories, proteins, etc ... and change colour 
        # (green for slimming, yellow for optimal and red for <<DANGER, you will be a fat person!>>) Definitly in POST method.
    if request.method=="GET":
        '''Show to user selectpicker class, let him choose products that 
        he want to add to menu'''
        products=FoodProduct.food.all()
        name_of_tables = func_name_of_tables(products)
        form=food_info()
        context={
            'products': products,
            'name_of_tables': name_of_tables,
            'form': form
        }
        return render(request, 'food_calculator/evaluate.html', context)
    else:
        '''Show to user all selected products. 
        Let him type weight of products that he wants to use for cooking (using jquery for this task)'''
        products=FoodProduct.food.all()
        name_of_tables = func_name_of_tables(products)
        form=food_info(request.POST)
        f = func_get_list_of_selected_products(form, products)
        context={
            'products': products,
            'name_of_tables': name_of_tables,
            'list_of_selected_products': f
        }
        return render(request, 'food_calculator/evaluate.html', context)






