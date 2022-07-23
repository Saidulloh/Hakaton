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
    CHOICES = (
        ('Developer', 'Developer'),
        ('Client', 'Client')
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    first_name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    email = models.EmailField() 
    phone_number = PhoneNumberField(
        max_length=13, 
        blank=True, 
        null=True
        )
    group = models.CharField(
        verbose_name='Тип пользователя',
        choices=CHOICES,
        max_length=10
    )
    avatar = models.ImageField(
        upload_to='dev_avatar/'
    )

    def __str__(self):
        return f'{self.pk} -- {self.username}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'


class Developer(User):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_developer',
        null=True, blank=True
    )
    CHOICES_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    DEV_LEVEL=(
        ('Junior','Junior'),
        ('Middle','Middle'),
        ('Senior','Senior'),
    )
    city = models.CharField(
        max_length=255
    )
    address = models.CharField(
        max_length=255
    )
    birth_date = models.DateField()
    direction = models.ManyToManyField(
        Direction, 
        related_name='dev_direction',
        null=True, blank=True
        )
    lvl = models.CharField(
        max_length=50,
        choices=DEV_LEVEL, 
        verbose_name='Уровень'
        )
    time_create = models.DateTimeField(
        'Время создания', 
        auto_now_add=True,
        )
    time_update = models.DateTimeField(
        'Время изменения', 
        auto_now=True,
        )
    gender = models.CharField(
        choices=CHOICES_GENDER,
        max_length=10,
        null=True,
        blank=True
    )
    nationality = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name= 'разработчик'
        verbose_name_plural = 'Разработчики'


class Client(User):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_client',
        null=True, blank=True
    )
    company = models.CharField(
        max_length=255
    )
    time_create = models.DateTimeField(
        'Время создания', 
        auto_now_add=True
        )
    time_update = models.DateTimeField(
        'Время изменения', 
        auto_now=True
        )

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'