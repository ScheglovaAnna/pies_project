# Generated by Django 3.2.6 on 2021-09-05 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pies_app', '0004_order_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pies',
        ),
    ]
