# Generated by Django 3.1.1 on 2020-10-23 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_calculator', '0021_auto_20201023_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmenu',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
