from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class Direction(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True
        )
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name='children'
        )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name= 'направление'
        verbose_name_plural = 'Направления'


class User(AbstractUser):
    CHOICES_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    DEV_LEVEL=(
        ('Junior','Junior'),
        ('Middle','Middle'),
        ('Senior','Senior'),
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    company = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    time_create = models.DateTimeField(
        'Время создания', 
        auto_now_add=True,
        )
    time_update = models.DateTimeField(
        'Время изменения', 
        auto_now=True,
        )
    address = models.CharField(
        max_length=255
        )
    city = models.CharField(
        max_length=255
        )
    email = models.EmailField() 
    phone_number = PhoneNumberField(
        max_length=13, 
        )
    avatar = models.ImageField(
        upload_to='dev_avatar/'
        )
    year = models.IntegerField(
        null=True
    )
    direction = models.ManyToManyField(
        Direction, 
        related_name='dev_direction',
        ) 
    lvl = models.CharField(
        max_length=50,
        choices=DEV_LEVEL, 
        verbose_name='Уровень'
        )
    gender = models.CharField(
        choices=CHOICES_GENDER,
        max_length=10,
        )
    nationality = models.CharField(
        max_length=255,
        null=True,
        blank=True
        )

    def __str__(self):
        return f'{self.pk} -- {self.username}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
