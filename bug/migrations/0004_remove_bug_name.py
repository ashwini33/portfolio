# Generated by Django 2.2.6 on 2019-11-15 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0003_auto_20191106_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='name',
        ),
    ]