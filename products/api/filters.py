import django_filters
from products.models import Product

class ProductFilter(django_filters.FilterSet):
    subcategory__category__id = django_filters.CharFilter(lookup_expr='iexact')
    subcategory__category__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['subcategory', "subcategory__category__id", "subcategory__category__name"]