# Generated by Django 2.2.6 on 2019-11-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0008_auto_20191115_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
