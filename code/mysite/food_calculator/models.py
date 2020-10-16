from django.db import models

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
    # search_field='title'
    # result_title_and_descrition=('title', 'text')
    # storytitles = models.Manager()

    def __str__(self):
        return self.prod_name

    # food = models.Manager()

    #def get_absolute_url(self):
        #return reverse()

    class Meta:
        verbose_name="Продукт"
        verbose_name_plural="Продукты"
        ordering=['prod_type','prod_name']