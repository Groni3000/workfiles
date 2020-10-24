from django import forms
from .models import ProductMenu
from .services import content_of_tables

'''
class DateInput(forms.DateInput):
    input_type='date'
'''

class display_food_name_form(forms.Form):
    display_food_name=forms.CharField()


class food_info(forms.Form):
    food_form=forms.MultipleChoiceField(choices=content_of_tables())

    class Meta():
        model = ProductMenu
        fields = ['list_of_selected_products_monday']


class Menu(forms.ModelForm):

    class Meta():
        model = ProductMenu
        fields = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday',
        'list_of_selected_products_monday', 
        'list_of_selected_products_tuesday',
        'list_of_selected_products_wednesday',
        'list_of_selected_products_thursday',
        'list_of_selected_products_friday',
        'list_of_selected_products_saturday',
        'list_of_selected_products_sunday'  
        ]