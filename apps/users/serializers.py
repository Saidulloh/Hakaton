from rest_framework import serializers

from apps.users.models import *


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class DeveloperMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'lvl',
            'direction',
        ]


class DeveloperFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
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


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']