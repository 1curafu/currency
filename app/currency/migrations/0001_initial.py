# Generated by Django 4.1.7 on 2023-04-02 12:16

import currency.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('email_from', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('request_method', models.CharField(max_length=255)),
                ('time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code_name', models.CharField(max_length=64, unique=True)),
                ('source_url', models.URLField(max_length=255)),
                ('country', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('avatar', models.FileField(blank=True,
                                            default=None,
                                            null=True,
                                            upload_to=currency.models.avatar_path)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'Euro'), (2, 'Dollar'),
                                                                       (3, 'Swiss Franc'), (4, 'Pound sterling')],
                                                              default=2)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sale', models.DecimalField(decimal_places=2, max_digits=6)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='rates',
                                             to='currency.source')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
