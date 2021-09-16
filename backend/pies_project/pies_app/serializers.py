from rest_framework import serializers, generics
# from rest_framework.fields import ReadOnlyField

from .models import *


class userListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class piesListSerializer(serializers.ModelSerializer):
    produser = serializers.CharField(source='get_produser_display')
    have = serializers.CharField(source='get_have_display')

    class Meta:
        model = Pies
        fields = "__all__"


class CreatePiesSerializer(serializers.ModelSerializer):
    # produser = serializers.CharField(source='get_produser_display')
    # have = serializers.CharField(source='get_have_display')
    class Meta:
        model = Pies
        fields = "__all__"


class PiesRetrieveSerializer(serializers.ModelSerializer):
    produser = serializers.CharField(source='get_produser_display')
    have = serializers.CharField(source='get_have_display')

    class Meta:
        model = Pies
        fields = "__all__"


class orderListSerializer(serializers.ModelSerializer):
    #pies_basket = serializers.SlugRelatedField(many=True)
    #pies_basket = serializers.SlugRelatedField(slug_field="name", read_only='True')
    pies_order = piesListSerializer(many=True, read_only=True)
    owner = userListSerializer()


    class Meta:
        model = Order
        fields = "__all__"


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

# class basketRelatedSerializer(serializers.ModelSerializer):
#     pies_basket = serializers.StringRelatedfields(many=True)
#
#     class Meta:
#         model = Basket
#         fields = "__all__"
