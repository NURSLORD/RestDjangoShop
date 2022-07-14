from rest_framework.serializers import ModelSerializer

from .models import Category, SubCategory, Product, Customer, Order, ItemOrders


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'sub_category', 'title', 'gender', 'is_popular',
                  'article', 'amount', 'old_price', 'new_price', 'cur', 'pub_date', 'image']


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ItemOrdersSerializer(ModelSerializer):
    class Meta:
        model = ItemOrders
        fields = "__all__"
