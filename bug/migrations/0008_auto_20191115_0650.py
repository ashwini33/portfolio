# Generated by Django 2.2.6 on 2019-11-15 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0007_auto_20191115_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
