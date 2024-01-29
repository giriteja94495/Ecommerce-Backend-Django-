from rest_framework import serializers
from .models import CartItem, Product, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','fullname','email','password', 'phonenumber', 'age','gender')


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return {'rate': obj.likes, 'count': obj.likes}

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'category', 'image', 'likes', 'rating')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','userId', 'product_id', 'quantity', 'added_at']