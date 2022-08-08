from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from apps.favorites.models import Favorite

User = get_user_model()

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        read_only_fields = ('id', 'user',)
        fields = '__all__'

    def create(self, validated_data):
        favorites = Favorite.objects.filter(user = validated_data['user'], fav_user = validated_data['fav_user'])
        if validated_data['user'].id != validated_data['fav_user'].id:
            if not favorites:
                return super().create(validated_data)


class FavoriteFullSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    favorite_user = FavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        read_only_fields = ('id')
        fields = ('id', 'create_at', 'fav_user', 'user')