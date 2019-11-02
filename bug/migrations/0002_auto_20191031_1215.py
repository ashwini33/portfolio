# Generated by Django 2.2.6 on 2019-10-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='name',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='bug',
            name='reference',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bug',
            name='solution',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bug',
            name='visual',
            field=models.ImageField(blank=True, null=True, upload_to='bug/images'),
        ),
    ]
