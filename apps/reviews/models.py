from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Review(models.Model):
    CHICES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    review = models.CharField(
        max_length=255
        )

    to_user = models.ForeignKey(
        User,
        related_name='to_user',
        on_delete=models.CASCADE
        )
    owner = models.ForeignKey(
        User, 
        related_name='owner_review',
        on_delete=models.PROTECT,
        null=True, blank=True
        )
    star = models.CharField(
        choices=CHICES, 
        max_length=10
        )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Owner {self.owner} -- to {self.to_user}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'