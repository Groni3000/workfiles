from django.shortcuts import render, redirect
from .models import FoodProduct, ProductMenu
from .forms import Menu, food_info, display_food_name_form
from .services import make_list_of_selected_products

# Create your views here.
def evaluate(request):
# PLANS:
# - Make a 'progress bar' for autheticated users (using his values: height, weight, age and something else?) that accumulates all values of
# calories, proteins, etc ... and change colour 
# (green for slimming, yellow for optimal and red for <<DANGER, you will be a fat person!>>) Definitly in POST method.
    if request.method=="GET":
        if request.user.is_authenticated:
            '''Show to user selectpicker class, let him choose products that 
            he want to add to menu'''
            menu_form=Menu()
            # weekly_form=week_form()
            # select_products_form=list_of_selected_products_form()
            context={
                'form': menu_form
            }
            return render(request, 'food_calculator/evaluate.html', context)
        else:
            form_to_select_food=food_info()

            context={
                'form': form_to_select_food
            }
            return render(request, 'food_calculator/evaluate.html', context)
    else:
        '''Show to user all selected products. 
        Let him type weight of products that he wants to use for cooking (using jquery for this task)'''
        if request.user.is_authenticated:
            form=Menu(request.POST)
            user=request.user
            if form.is_valid():
                menu=form.save(commit=False)
                menu.user=user
                menu.save()
                form.save_m2m()
                print('example created')
            context={
            }
            return redirect('profile', username=user)
        else:
            selected_product_names=food_info(request.POST)
            if selected_product_names.is_valid():
                selected_product_names_list=selected_product_names.cleaned_data.get('food_form')
                selected_products_list=make_list_of_selected_products(selected_product_names_list)
            
            context={
                'selected_products_list': selected_products_list
            }
            return render(request, 'food_calculator/evaluate.html', context)

        
        
        




