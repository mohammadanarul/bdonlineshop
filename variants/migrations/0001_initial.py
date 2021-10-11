# Generated by Django 3.2.8 on 2021-10-11 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colors', '0001_initial'),
        ('sizes', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('image_id', models.IntegerField(blank=True, null=True, verbose_name='image id')),
                ('price', models.FloatField(blank=True, default=1, null=True, verbose_name='price')),
                ('quantity', models.IntegerField(default=1)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colors.color', verbose_name='color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sizes.size', verbose_name='size')),
            ],
        ),
    ]