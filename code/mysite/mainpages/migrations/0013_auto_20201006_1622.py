# Generated by Django 3.1.1 on 2020-10-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0012_auto_20201006_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile_phone',
            name='specification',
        ),
        migrations.AddField(
            model_name='mobile_phone',
            name='display',
            field=models.IntegerField(choices=[(5, 'HD, 1280x720p'), (12, 'FullHD, 1920x1080p')], default=5),
        ),
        migrations.AddField(
            model_name='mobile_phone',
            name='resolution',
            field=models.CharField(choices=[('1280x720', 'HD, 1280x720p'), ('1920x1080', 'FullHD, 1920x1080p'), ('2560x1440', 'QuadHD, 2560x1440p')], default='1920x1080', max_length=300),
        ),
    ]