# Generated by Django 3.0.5 on 2021-08-11 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0005_wishlist_wished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='wished',
        ),
    ]
