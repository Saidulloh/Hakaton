from rest_framework import serializers

from apps.review.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        read_only_fields = ('id', 'owner')
        fields = (
            'id',
            'review',
            'star',
            'create_at',
            'owner',
        )