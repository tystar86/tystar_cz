# Generated by Django 2.2 on 2019-04-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190411_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
