# import Python's datetime module


# list_of_choices=[
#         [i,
#         [
#             [j,j] for j in range(1, 3) 
#         ]
#         ] for i in range(3)] 


# for i in range(len(list_of_choices)):
#     print(list_of_choices[i])



# for i in range(len(list_of_choices)):
#     for j in range(len(list_of_choices[i][1])):
#         list_of_choices[i][1][j]=tuple(list_of_choices[i][1][j])
#     list_of_choices[i][1]=tuple(list_of_choices[i][1])
#     list_of_choices[i]=tuple(list_of_choices[i])


# print('_________________________________')

# for i in range(len(list_of_choices)):
#     print(list_of_choices[i])

#                <!-- <textarea class="form-control" style="width: 300%;" rows='3' id="names-of-selected" readonly></textarea> -->

# a=[1,1,1,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9,10,10,10]
# name_T=[]
# for i in range()
# name_T=[i for i in a if i not in name_T ]
# print(name_T)


'''
<div class="info">
    {% if request.method == "GET" %}
    {% else %}
    {% for el in list_of_selected_products %}
    <div class="form-inline">
        <div class="col-10">
            <input class="form-control" style="width: 100%;" type="text" id="selected-prod_name-{{el}}" value="{{el}}" readonly>
        </div>
        <!-- 2 HIDDEN INPUTS WITH INFORMATION -->
            <!-- First -->
        <input class="all-info" type="text" value="{{el}};{{el.prod_calories}};{{el.prod_proteins}};{{el.prod_fats}};{{el.prod_carbohydrates}}" hidden>
            <!-- end of first -->
        <div class="col-2">
            <input class="form-control-multiplier" type="number" step="0.01" id="weight_of_selected-prod_name-{{el}}" placeholder="Введите вес (гр.):">
            <!-- Second -->
            <input class="form-control multiplier" type="number" step="0.01" id="weight_of_selected-prod_name-{{el}}" value="0" hidden>
            <!-- end of second -->
        </div>
        <!-- END OF 2 INPUTS WITH INFORMATION-->
    </div>
    {% endfor %}
    <!-- Summury calories, proteins, etc ... -->
    <p class="mt-4" id='explaining-text'>За выбранное количество выбранных продуктов Вы употребите:</p>
    <div class="form-inline">
        <input class="form-control" type="text" id="selected-prod_calories" value="0" readonly>
        <label class="ml-2" for="selected-prod_calories"> калорий;</label>
    </div>
    <div class="form-inline">
        <input class="form-control" type="text" id="selected-prod_proteins" value="0" readonly>
        <label class="ml-2" for="selected-prod_proteins"> белков;</label>
    </div>
    <div class="form-inline">
        <input class="form-control" type="text" id="selected-prod_fats" value="0" readonly>
        <label class="ml-2" for="selected-prod_fats"> жиров;</label>
    </div>
    <div class="form-inline">
        <input class="form-control" type="text" id="selected-prod_carbohydrates" value="0" readonly>
        <label class="ml-2" for="selected-prod_carbohydrates"> углеводов;</label>
    </div>
    <!-- end of summury calories, proteins, etc ... -->
    {% endif %}
</div>
'''




'''
{% if user.is_authenticated %}
<form action="{% url 'eval' %}", method="POST">
    {% csrf_token %}
    <div class="form-group row">
        <label for="example-date-input" class="col-1 col-form-label">{{field.name}}</label>
        <div class="col-8">
            {% for field in weekly_form %}
                <div class="mt-2">
                    {% render_field field class="form-control" style="width:23%" type="date" %}
                </div>
            {% endfor %}
        </div>
        <div class="col-3">
            {% for field in selected_products_form %}
                <div class="mt-2">
                    {% render_field field type="select" class="selectpicker" name="food" data-style="btn-primary" data-width="auto" multiple="true" data-selected-text-format="count > 2" data-live-search="true" data-actions-box="true"%}
                </div>
            {% endfor %}
        </div>
    </div>
    <button class="btn btn-primary" type='submit'>Submit</button>
</form>
{% else %}
{% endif %}
'''



'''
                    <table class="table table-striped">
                        <tr>
                            <th>Day</th>
                            <th>Date:</th>
                            <td><button type="submit" class="btn btn-default">Submit</button></td>
                        </tr>
                        <tr class="cpy">
                            <td>
                                {% for field in weekly_form %}
                                        <label for="example-date-input" class="col-2 col-form-label mt-2">{{field.name}}</label>
                                        {% render_field field class="form-control" style="width:100%" type="date" %}
                                {% endfor %}
                            </td>
                            <td>
                                {% for field in select_products_form %}
                                    {% render_field field type="select" class="selectpicker mt-5" name="food" data-style="btn-primary" data-width="250px" multiple="true" data-selected-text-format="count > 2" data-live-search="true" data-actions-box="true"%}
                                {% endfor %}
                            </td>
                        </tr>
                    </table>
'''














#forms.py
# from django import forms
# from .models import ProductMenu
# from .services import content_of_tables

# '''
# class DateInput(forms.DateInput):
#     input_type='date'
# '''

# class display_food_name_form(forms.Form):
#     display_food_name=forms.CharField()


# class food_info(forms.Form):
#     food_form=forms.MultipleChoiceField(choices=content_of_tables())

#     class Meta():
#         model = ProductMenu
#         fields = ['list_of_selected_products_monday']

# class week_form(forms.Form):
#     monday=forms.DateField(required=False)
#     tuesday=forms.DateField(required=False)
#     wednesday=forms.DateField(required=False)
#     thursday=forms.DateField(required=False)
#     friday=forms.DateField(required=False)
#     saturday=forms.DateField(required=False)
#     sunday=forms.DateField(required=False)

# class list_of_selected_products_form(forms.Form): 
#     list_of_selected_products_monday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_tuesday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_wednesday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_thursday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_friday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_saturday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_sunday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)


# class Menu(forms.ModelForm):
#     monday=forms.DateField(required=False)
#     tuesday=forms.DateField(required=False)
#     wednesday=forms.DateField(required=False)
#     thursday=forms.DateField(required=False)
#     friday=forms.DateField(required=False)
#     saturday=forms.DateField(required=False)
#     sunday=forms.DateField(required=False)
#     list_of_selected_products_monday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_tuesday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_wednesday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_thursday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_friday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_saturday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)
#     list_of_selected_products_sunday=forms.MultipleChoiceField(choices=content_of_tables(), required=False)

#     class Meta():
#         model = ProductMenu
#         fields = ['monday', 'tuesday', 'wednesday',
#         'thursday', 'friday', 'saturday', 'sunday',
#         'list_of_selected_products_monday', 
#         'list_of_selected_products_tuesday',
#         'list_of_selected_products_wednesday',
#         'list_of_selected_products_thursday',
#         'list_of_selected_products_friday',
#         'list_of_selected_products_saturday',
#         'list_of_selected_products_sunday'  
#         ]

# # models.py

# from django.db import models
# from datetime import datetime, date
# from users.models import CustomUser


# # Create your models here.
# # Took info from this site: http://frs24.ru/st/tablica-kalorijnosti-produktov-pitaniya/#101
# class FoodProduct(models.Model):
#     id = models.AutoField(primary_key=True)
#     prod_name=models.CharField(max_length=300, blank=True)
#     prod_type=models.CharField(max_length=300, blank=True)
#     prod_calories=models.DecimalField(max_digits=6, decimal_places=2, blank=True)
#     prod_proteins=models.DecimalField(max_digits=6, decimal_places=2, blank=True)
#     prod_fats=models.DecimalField(max_digits=6, decimal_places=2, blank=True)
#     prod_carbohydrates=models.DecimalField(max_digits=6, decimal_places=2, blank=True)

#     #TODO Maybe, later I should use it. Maybe!
#     # search_field='Name of field'
#     # fields_for_result_of_search_for_html=('Name of field', 'Name of field')

#     def __str__(self):
#         return self.prod_name

#     food = models.Manager()

#     #def get_absolute_url(self):
#         #return reverse()

#     class Meta:
#         verbose_name="Продукт"
#         verbose_name_plural="Продукты"
#         ordering=['prod_type','prod_name']


# class ProductMenu(models.Model):
#     id = models.AutoField(primary_key=True)
#     timestamp=models.DateField(auto_now_add=True)
#     monday=models.DateField("Понедельник", blank=True, null=True)
#     tuesday=models.DateField("Вторник", blank=True, null=True)
#     wednesday=models.DateField("Среда", blank=True, null=True)
#     thursday=models.DateField("Четверг", blank=True, null=True)
#     friday=models.DateField("Пятница", blank=True, null=True)
#     saturday=models.DateField("Суббота", blank=True, null=True)
#     sunday=models.DateField("Воскресенье", blank=True, null=True)
#     user=models.ForeignKey('users.CustomUser', on_delete=models.PROTECT, default=None)
#     list_of_selected_products_monday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на понедельник", related_name='monday+', blank=True, default=None)
#     list_of_selected_products_tuesday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на вторник", related_name='tuesday+', blank=True, default=None)
#     list_of_selected_products_wednesday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на среду", related_name='wednesday+', blank=True, default=None)
#     list_of_selected_products_thursday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на четверг", related_name='thursday+', blank=True, default=None)
#     list_of_selected_products_friday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на пятницу", related_name='friday+', blank=True, default=None)
#     list_of_selected_products_saturday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на субботу", related_name='saturday+', blank=True, default=None)
#     list_of_selected_products_sunday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на воскресенье", related_name='sunday+', blank=True, default=None)
    
#     def __str__(self):
#         self.name=str(self.user)+', '+str(self.timestamp)
#         return self.name

#     product_menu=models.Manager()

#     class Meta():
#         verbose_name="Меню продуктов на неделю"
#         verbose_name_plural="Меню продуктов на неделю"
#         ordering=["timestamp"]
#         constraints = [
#             models.CheckConstraint(check=models.Q(monday__iso_week_day=1, monday__isnull=False) | models.Q(monday__isnull=True), name='check_monday'),
#             models.CheckConstraint(check=models.Q(tuesday__iso_week_day=2, monday__isnull=False) | models.Q(tuesday__isnull=True), name='check_tuesday'),
#             models.CheckConstraint(check=models.Q(wednesday__iso_week_day=3, wednesday__isnull=False) | models.Q(wednesday__isnull=True), name='check_wednesday'),
#             models.CheckConstraint(check=models.Q(thursday__iso_week_day=4, thursday__isnull=False) | models.Q(thursday__isnull=True), name='check_thursday'),
#             models.CheckConstraint(check=models.Q(friday__iso_week_day=5, friday__isnull=False) | models.Q(friday__isnull=True), name='check_friday'),
#             models.CheckConstraint(check=models.Q(saturday__iso_week_day=6, saturday__isnull=False) | models.Q(saturday__isnull=True), name='check_saturday'),
#             models.CheckConstraint(check=models.Q(sunday__iso_week_day=7, sunday__isnull=False) | models.Q(sunday__isnull=True), name='check_sunday')
#             ]