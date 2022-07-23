# Generated by Django 4.0.6 on 2022-07-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_group_developer_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='group',
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.CharField(choices=[('Developer', 'Developer'), ('Client', 'Client')], default=1, max_length=10, verbose_name='Тип пользователя'),
            preserve_default=False,
        ),
    ]