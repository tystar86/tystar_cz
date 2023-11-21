# Generated by Django 5.1 on 2023-11-18 09:13

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField(blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title'])),
                ('resources', models.ManyToManyField(blank=True, to='my_site.resource')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]