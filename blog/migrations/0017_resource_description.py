# Generated by Django 2.2 on 2019-04-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_resource_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
