from rest_framework import serializers

from apps.users.models import *
from apps.review.serializers import ReviewSerializer


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class DeveloperMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = [
            'id',
            'username',
            'lvl',
            'direction',
        ]


class DeveloperFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = [
            'id',
            'avatar',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'city',
            'birth_date',
            'direction',
            'lvl',
            'time_create',
            'gender',
            'nationality',
            'password',
        ]
        
    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class DeveloperShowSerializer(serializers.ModelSerializer):
    review_dev = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Developer
        fields = [
            'id',
            'avatar',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'city',
            'birth_date',
            'direction',
            'lvl',
            'time_create',
            'gender',
            'nationality',
            'password',
            'review_dev',
        ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'avatar',
            'email',
            'phone_number',
            'company',
            'password'
        ]

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user