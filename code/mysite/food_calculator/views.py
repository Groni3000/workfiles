from django.shortcuts import render

# Create your views here.
def evaluate(request):
    if request.method=="POST":
        # form=MY FORM(request.POST)
        return render(request, 'food_calculator/evaluate.html')
    return render(request, 'food_calculator/evaluate.html')