# Generated by Django 3.1.2 on 2020-10-13 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='business_id',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
