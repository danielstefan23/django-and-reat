# Generated by Django 3.2.4 on 2021-06-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fav_color',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]