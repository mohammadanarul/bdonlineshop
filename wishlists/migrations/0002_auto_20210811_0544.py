# Generated by Django 3.0.5 on 2021-08-10 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='slug',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
