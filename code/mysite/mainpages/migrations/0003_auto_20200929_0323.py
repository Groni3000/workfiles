# Generated by Django 3.1.1 on 2020-09-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0002_remove_stories_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='UserId',
            field=models.IntegerField(default=1),
        ),
    ]
