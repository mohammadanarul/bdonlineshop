# Generated by Django 3.0.5 on 2021-07-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('code', models.CharField(max_length=50, verbose_name='code')),
            ],
        ),
    ]
