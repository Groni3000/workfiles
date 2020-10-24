from django.contrib import admin
from .models import FoodProduct, ProductMenu

# Register your models here.

admin.site.register(FoodProduct)
admin.site.register(ProductMenu)