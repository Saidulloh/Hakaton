from rest_framework import serializers

from apps.favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        read_only_fields = ('id', 'user',)
        fields = '__all__'


class FavoriteFullSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    favorite_user = FavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        read_only_fields = ('id', 'user')
        fields = '__all__'