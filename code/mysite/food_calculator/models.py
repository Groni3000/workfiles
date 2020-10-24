from django.db import models
from datetime import datetime, date
from users.models import CustomUser
#from .services import content_of_tables

# Create your models here.
# Took info from this site: http://frs24.ru/st/tablica-kalorijnosti-produktov-pitaniya/#101
class FoodProduct(models.Model):
    id = models.AutoField(primary_key=True)
    prod_name=models.CharField(max_length=300, blank=True)
    prod_type=models.CharField(max_length=300, blank=True)
    prod_calories=models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    prod_proteins=models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    prod_fats=models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    prod_carbohydrates=models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    #TODO Maybe, later I should use it. Maybe!
    # search_field='Name of field'
    # fields_for_result_of_search_for_html=('Name of field', 'Name of field')

    def __str__(self):
        return self.prod_name

    food = models.Manager()

    #def get_absolute_url(self):
        #return reverse()

    class Meta:
        verbose_name="Продукт"
        verbose_name_plural="Продукты"
        ordering=['prod_type','prod_name']


class ProductMenu(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp=models.DateField(auto_now_add=True)
    monday=models.DateField("Понедельник", blank=True, null=True)
    tuesday=models.DateField("Вторник", blank=True, null=True)
    wednesday=models.DateField("Среда", blank=True, null=True)
    thursday=models.DateField("Четверг", blank=True, null=True)
    friday=models.DateField("Пятница", blank=True, null=True)
    saturday=models.DateField("Суббота", blank=True, null=True)
    sunday=models.DateField("Воскресенье", blank=True, null=True)
    list_of_selected_products_monday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на понедельник", related_name='monday', blank=True, default=None)
    list_of_selected_products_tuesday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на вторник", related_name='tuesday', blank=True, default=None)
    list_of_selected_products_wednesday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на среду", related_name='wednesday', blank=True, default=None)
    list_of_selected_products_thursday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на четверг", related_name='thursday', blank=True, default=None)
    list_of_selected_products_friday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на пятницу", related_name='friday', blank=True, default=None)
    list_of_selected_products_saturday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на субботу", related_name='saturday', blank=True, default=None)
    list_of_selected_products_sunday=models.ManyToManyField('FoodProduct',verbose_name="Лист продуктов на воскресенье", related_name='sunday', blank=True, default=None)
    user=models.ForeignKey('users.CustomUser', on_delete=models.PROTECT, default=None)

    def __str__(self):
        self.name=str(self.user)+', '+str(self.timestamp)
        return self.name

    product_menu=models.Manager()

    class Meta():
        verbose_name="Меню продуктов на неделю"
        verbose_name_plural="Меню продуктов на неделю"
        ordering=["timestamp"]
        constraints = [
            models.CheckConstraint(check=models.Q(monday__iso_week_day=1, monday__isnull=False) | models.Q(monday__isnull=True), name='check_monday'),
            models.CheckConstraint(check=models.Q(tuesday__iso_week_day=2, monday__isnull=False) | models.Q(tuesday__isnull=True), name='check_tuesday'),
            models.CheckConstraint(check=models.Q(wednesday__iso_week_day=3, wednesday__isnull=False) | models.Q(wednesday__isnull=True), name='check_wednesday'),
            models.CheckConstraint(check=models.Q(thursday__iso_week_day=4, thursday__isnull=False) | models.Q(thursday__isnull=True), name='check_thursday'),
            models.CheckConstraint(check=models.Q(friday__iso_week_day=5, friday__isnull=False) | models.Q(friday__isnull=True), name='check_friday'),
            models.CheckConstraint(check=models.Q(saturday__iso_week_day=6, saturday__isnull=False) | models.Q(saturday__isnull=True), name='check_saturday'),
            models.CheckConstraint(check=models.Q(sunday__iso_week_day=7, sunday__isnull=False) | models.Q(sunday__isnull=True), name='check_sunday')
            ]