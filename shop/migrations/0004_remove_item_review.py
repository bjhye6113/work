# Generated by Django 2.1.7 on 2019-04-28 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190428_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='review',
        ),
    ]
