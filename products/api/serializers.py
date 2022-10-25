from rest_framework import serializers
from products.models import Product, Subcategory, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Subcategory
        fields = ("id", "name", "category")


class ProductSerializer(serializers.ModelSerializer):
    # total_price_ = serializers.ReadOnlyField(source="total_price")
    total_price = serializers.SerializerMethodField()
    subcategory = SubcategorySerializer()
    detail = serializers.HyperlinkedIdentityField(view_name='products-api:detail', lookup_field="slug")


    class Meta:
        model = Product
        fields = "__all__"

    def get_total_price(self, obj):
        tax_price = obj.tax_price if obj.tax_price else 0
        discount_price = obj.discount_price if obj.discount_price else 0
        return obj.price + tax_price - discount_price