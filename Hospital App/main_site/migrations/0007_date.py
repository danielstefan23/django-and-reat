# Generated by Django 2.2.24 on 2022-01-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_auto_20220109_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('availability', models.BooleanField()),
            ],
        ),
    ]
