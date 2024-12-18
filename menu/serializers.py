from .models import BigMenu, SmallMenu, Product
from django.contrib.auth.models import User
from rest_framework import serializers


class BigMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigMenu
        fields = '__all__'  # Barcha maydonlarni qo'shish


class SmallMenuSerializer(serializers.ModelSerializer):
    bigmenu = BigMenuSerializer()  # BigMenu haqida to'liq ma'lumot olish

    class Meta:
        model = SmallMenu
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ProductSerializer(serializers.ModelSerializer):
    smallmenu = SmallMenuSerializer()  # SmallMenu haqida to'liq ma'lumot olish

    class Meta:
        model = Product
        fields = '__all__'
