# Generated by Django 3.1.1 on 2020-10-16 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodproduct',
            options={'ordering': ['prod_type', 'prod_name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
