from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from ...models import paintforcar

class Command(BaseCommand):
    help = 'Adding data to database'

    def handle(self, *args, **options):
        try:
            for k in range(82):
                if k==0:
                    url='https://avtomaler-plus.com.ua/vse-dly-pokraski/'
                else:
                    url='https://avtomaler-plus.com.ua/vse-dly-pokraski/?page='+str(k)
                result=requests.get(url)
                src=result.content
                soup=BeautifulSoup(src,'lxml')
                products=soup.find_all('div', attrs={'class':'name'})
                for i in products:
                    p=paintforcar(nameofpaint=i.text)
                    p.save()
                
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')