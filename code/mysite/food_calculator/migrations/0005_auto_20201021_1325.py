# Generated by Django 3.1.1 on 2020-10-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_calculator', '0004_auto_20201021_1309'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='testdateclass',
            managers=[
            ],
        ),
        migrations.RemoveConstraint(
            model_name='testdateclass',
            name='day_of_the_week_fits',
        ),
        migrations.AlterField(
            model_name='testdateclass',
            name='test_date',
            field=models.DateField(null=True),
        ),
        migrations.AddConstraint(
            model_name='testdateclass',
            constraint=models.CheckConstraint(check=models.Q(test_date__iso_week_day=1), name='day_of_the_week_fits'),
        ),
    ]