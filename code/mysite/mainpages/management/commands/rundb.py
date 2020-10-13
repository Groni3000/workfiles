from django.core.management.base import BaseCommand, CommandError
from ...models import stories
import requests, json
from requests.exceptions import HTTPError

class Command(BaseCommand):
    help = 'Adding data to database'

    def handle(self, *args, **options):
        try:
            i=1
            for k in range(100):
                url='https://jsonplaceholder.typicode.com/todos/'+str(k+1)
                response = requests.get(url)
                response.raise_for_status()
                # access JSOn content
                jsonResponse = response.json()
                if jsonResponse["completed"]==True:
                    userId=jsonResponse['userId']
                    
                    titleId=jsonResponse['id']
                    
                    title=jsonResponse['title']
                    
                    story=stories(i,userId,title,titleId) #TODO Why am I supposed to type increment for AUTO-ID?????? Strange, need to test.
                    story.save()
                    i=i+1
            
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')