# Generated by Django 2.2.24 on 2022-01-10 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='availability',
        ),
    ]
