from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserAuthenticationForm
from django.contrib.auth import login, logout, authenticate
from food_calculator.models import ProductMenu, FoodProduct
from .services import prepared_results


# Create your views here.

def signup_view(request):
    '''Displaying form for user creation and savint him to database'''
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home_page')
    else:
        form=CustomUserCreationForm()
    context={
        'form': form
    }
    return render(request, 'users/signup.html', context)

def log_in_view(request):
    if request.method=="POST":
        form=CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form=CustomUserAuthenticationForm()
    context={
        'form' : form,
    }
    return render(request, 'users/log_in.html', context)

def log_out_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('home_page')

def profile_view(request, username):
    user=request.user
    user_product_menus=ProductMenu.product_menu.filter(user__username__iexact=user)
    user_results = prepared_results(user_product_menus)

    context={
        'username' : username,
        'user_results': user_results,
    }
    return render(request, 'users/profile_page.html', context)

def menu_overview_view(request, username, id_menu):

    context={
        'username': username,
        'id_menu': id_menu
    }
    return render(request, 'users/menu_overview.html', context)