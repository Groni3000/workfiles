from django import forms

class food_info(forms.Form):
    food_form=forms.CharField(max_length=300)