# Generated by Django 2.2.24 on 2022-01-03 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_user_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='identifier',
            new_name='specializare',
        ),
    ]