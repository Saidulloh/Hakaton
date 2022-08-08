from django.db import models
from django.contrib.auth import get_user_model

from apps.users.models import User


User = get_user_model()


class Favorite(models.Model):
    fav_user = models.ForeignKey(
        User,
        related_name='favorite_user',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner'
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.fav_user.id} -- {self.user.id}'

    class Meta:
        ordering=['-create_at']