# Generated by Django 4.0.6 on 2022-07-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='birth_date',
            field=models.DateField(),
        ),
    ]
