from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserAuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.

def signup_view(request):
    '''Displaying form for user creation and savint him to database'''
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            #log the user signed up
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
