# Generated by Django 3.1.1 on 2020-10-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0014_auto_20201006_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paintforcar',
            name='nameofpaint',
        ),
        migrations.AddField(
            model_name='paintforcar',
            name='Наименование',
            field=models.CharField(default='', help_text='Введите наименование краски', max_length=300),
        ),
    ]
