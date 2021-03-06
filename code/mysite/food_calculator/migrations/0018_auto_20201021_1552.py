# Generated by Django 3.1.1 on 2020-10-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_calculator', '0017_auto_20201021_1546'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='productmenu',
            name='check_monday',
        ),
        migrations.RemoveConstraint(
            model_name='productmenu',
            name='check_tuesday',
        ),
        migrations.RemoveConstraint(
            model_name='productmenu',
            name='check_wednesday',
        ),
        migrations.RemoveConstraint(
            model_name='productmenu',
            name='check_thursday',
        ),
        migrations.RemoveConstraint(
            model_name='productmenu',
            name='check_friday',
        ),
        migrations.RemoveConstraint(
            model_name='productmenu',
            name='check_saturday',
        ),
        migrations.RemoveConstraint(
            model_name='productmenu',
            name='check_sunday',
        ),
        migrations.AddConstraint(
            model_name='productmenu',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('monday__isnull', False), ('monday__iso_week_day', 1)), ('monday__isnull', True), _connector='OR'), name='check_monday'),
        ),
        migrations.AddConstraint(
            model_name='productmenu',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('monday__isnull', False), ('tuesday__iso_week_day', 2)), ('tuesday__isnull', True), _connector='OR'), name='check_tuesday'),
        ),
        migrations.AddConstraint(
            model_name='productmenu',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('wednesday__isnull', False), ('wednesday__iso_week_day', 3)), ('wednesday__isnull', True), _connector='OR'), name='check_wednesday'),
        ),
        migrations.AddConstraint(
            model_name='productmenu',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('thursday__isnull', False), ('thursday__iso_week_day', 4)), ('thursday__isnull', True), _connector='OR'), name='check_thursday'),
        ),
        migrations.AddConstraint(
            model_name='productmenu',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('friday__isnull', False), ('friday__iso_week_day', 5)), ('friday__isnull', True), _connector='OR'), name='check_friday'),
        ),
        migrations.AddConstraint(
            model_name='productmenu',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('saturday__isnull', False), ('saturday__iso_week_day', 6)), ('saturday__isnull', True), _connector='OR'), name='check_saturday'),
        ),
        migrations.AddConstraint(
            model_name='productmenu',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('sunday__isnull', False), ('sunday__iso_week_day', 7)), ('sunday__isnull', True), _connector='OR'), name='check_sunday'),
        ),
    ]
