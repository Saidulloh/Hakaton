from rest_framework import serializers

from apps.reviews.models import Review


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
            'to_user'
        )
        
    def create(self, validated_data):
        reviews = Review.objects.filter(owner = validated_data['owner'], to_user = validated_data['to_user'])
        if not reviews:
            return super().create(validated_data)
