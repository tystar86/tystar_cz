# Generated by Django 2.2 on 2019-04-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190412_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='aa'),
            preserve_default=False,
        ),
    ]
