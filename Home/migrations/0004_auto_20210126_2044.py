# Generated by Django 3.1.5 on 2021-01-27 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20210121_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbs',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='climbs',
            name='city',
            field=models.CharField(default='Austin', max_length=20),
        ),
    ]
