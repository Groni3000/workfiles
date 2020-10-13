from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from ...models import paintforcar

class Command(BaseCommand):
    help = 'Adding data to database'

    def handle(self, *args, **options):
        try:
            for k in range(1,50):
                url='https://irsmarket.ru/catalog/avtomobilnye_kraski/?limit=48&PAGEN_1='+str(k)
                result=requests.get(url)
                src=result.content
                soup=BeautifulSoup(src,'lxml')


                for i in soup.find_all('div', attrs={'class':'catalog-item-table-view'}):
                    prod_names=i.find_all('a', attrs={'class':'item-title'})
                    vendor_codes=i.find_all('div',attrs={'class': 'article'})
                
                for j in range(len(prod_names)):
                    p=paintforcar(nameofpaint=prod_names[j].attrs['title'],vendor_code=' '.join(vendor_codes[j].text.split()))
                    p.save()
                print('.', sep='',end='', flush=True)

                
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')