# Generated by Django 4.1.7 on 2023-04-05 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='email_from',
            new_name='email',
        ),
    ]
