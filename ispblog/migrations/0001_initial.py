# Generated by Django 4.2.4 on 2023-08-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=100)),
                ('speed', models.CharField(max_length=100)),
                ('ftp', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'services ',
                'ordering': ('id',),
            },
        ),
    ]
