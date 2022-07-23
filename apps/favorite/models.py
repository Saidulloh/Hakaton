from django.db import models
from django.contrib.auth import get_user_model

from apps.users.models import Developer


User = get_user_model()


class Favorite(models.Model):
    developer = models.ForeignKey(
        Developer,
        related_name='favorite_dev',
        on_delete=models.CASCADE,
        unique=True
    )
    user = models.ForeignKey(
        User,
        related_name='favorite_user',
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.developer.id} -- {self.user.username}'

    class Meta:
        ordering=['-create_at']