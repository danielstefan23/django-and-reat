# Generated by Django 2.2.24 on 2022-01-10 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_date'),
        ('login', '0008_auto_20220103_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_site.Date'),
        ),
    ]
