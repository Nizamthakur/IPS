# Generated by Django 4.2.4 on 2023-08-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ispblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]