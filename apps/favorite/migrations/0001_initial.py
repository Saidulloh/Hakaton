# Generated by Django 4.0.6 on 2022-07-23 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_remove_developer_language_alter_client_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_dev', to='users.developer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
    ]
