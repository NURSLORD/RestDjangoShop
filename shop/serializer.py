from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category, SubCategory, Product, Order, ItemOrders, Comment


class CategorySerializer(ModelSerializer):
    sub_categories = serializers.SerializerMethodField('get_sub_categories')

    class Meta:
        model = Category
        fields = ['title', 'sub_categories', 'is_active']

    def get_sub_categories(self, obj):
        sub_categories = SubCategory.objects.filter(category=obj)
        return SubCategorySerializer(sub_categories, many=True).data


class CatSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class SubSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'title']


class ProSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'title']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'is_active']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'sub_category', 'title', 'gender', 'is_popular',
                  'article', 'amount', 'old_price', 'new_price', 'cur', 'pub_date', 'image']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ItemOrdersSerializer(ModelSerializer):
    class Meta:
        model = ItemOrders
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
