from django import forms

class result_of_search_page(forms.Form):
    search_vendorcode=forms.CharField(max_length=300)