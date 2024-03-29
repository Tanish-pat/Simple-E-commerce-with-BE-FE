from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item, Order, Profile, Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def createUser(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def updateUser(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
    
    def deleteUser(self, instance):
        instance.delete()
        return instance
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "price", "description", "image", "added_at", "buyer"]
        extra_kwargs = {'added_at': {'read_only': True}, 'buyer': {'read_only': True}}