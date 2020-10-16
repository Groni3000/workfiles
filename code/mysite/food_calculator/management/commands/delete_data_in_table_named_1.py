from django.core.management.base import BaseCommand, CommandError
import importlib



class Command(BaseCommand):
    help = 'Deleting all data in table'

    def add_arguments(self, parser):
        parser.add_argument('table_names', nargs='+', type=str)

    def handle(self, *args, **options):
        for table_name in options['table_names']:
            table = getattr(importlib.import_module('...models','food_calculator.managment.commands'), table_name)
            try:
                table._base_manager.all().delete()
            except table.DoesNotExist:
                raise CommandError('Table "%s" does not exist' % table)
        