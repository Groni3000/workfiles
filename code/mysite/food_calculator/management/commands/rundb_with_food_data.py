from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from ...models import FoodProduct

class Command(BaseCommand):
    help = 'Adding food_data to database'

    def handle(self, *args, **options):
        try:
            url='http://frs24.ru/st/tablica-kalorijnosti-produktov-pitaniya/#101'
            result=requests.get(url)
            src=result.content
            soup=BeautifulSoup(src,'lxml')
            
            all_prod_types=soup.find_all('div', attrs={'align': 'center', 'class': 'z1'})
            all_prod_tables=soup.find_all('table', attrs={'class': 'norm'})
            all_elements_of_tables=soup.find_all(lambda tag: tag.name=='td'and not tag.attrs and len(tag)>0 and len(tag.findChildren())==0)
            list_of_len=[len(i)-1 for i in all_prod_tables]

            summing=0
            
            for k in range(len(list_of_len)):
                prod_type="Таблица "+' '.join(all_prod_types[k].text.split('\n')[0].split(' ')[1:])
                l=1
                for el in range(summing, (summing+(list_of_len[k])*5)):
                    if l>5:
                        l=1
                    if l==1:
                        prod_name=all_elements_of_tables[el].text
                        l=l+1
                    elif l==2:
                        prod_calories=all_elements_of_tables[el].text
                        l=l+1
                    elif l==3:
                        prod_proteins=all_elements_of_tables[el].text
                        l=l+1
                    elif l==4:
                        prod_fats=all_elements_of_tables[el].text
                        l=l+1
                    elif l==5:
                        prod_carbohydrates=all_elements_of_tables[el].text
                        l=l+1
                        new_food_prod=FoodProduct(
                        prod_name=prod_name,
                        prod_type=prod_type,
                        prod_calories=prod_calories,
                        prod_proteins=prod_proteins,
                        prod_fats=prod_fats,
                        prod_carbohydrates=prod_carbohydrates
                        )
                        new_food_prod.save()
                        print('.', sep='',end='', flush=True)
                print("От", summing, "до", summing+(list_of_len[k])*5, flush=True)
                summing=summing+(list_of_len[k])*5
                
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')