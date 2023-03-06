# Generated by Django 4.1.7 on 2023-02-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('source_url', models.URLField(max_length=255)),
                ('country', models.CharField(max_length=64)),
            ],
        ),
    ]