from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductCreateSerializer
from products.models import Product
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from .paginations import CustomPagination


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    # pagination_class = CustomPagination

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     queryset = Product.objects.all()
    #     # category = request.GET.get("category", None)
    #     # search = request.GET.get("search", None)
    #     # if category:
    #     #     queryset = queryset.filter(subcategory__category__id=int(category))
    #     return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializer
        return ProductCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"

    # def perform_update(self, serializer):
    #     return serializer.save()




class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (IsAuthenticated, )

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_product = serializer.save(user=request.user)
        print(new_product.name)
        return Response(serializer.data, status=201)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = "slug"

    # def get_object(self):
    #     slug = self.kwargs.get("slug")
    #     obj = Product.objects.get(slug=slug)
    #     return obj

    def put(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.serializer_class(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)




class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = "slug"



class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = "slug"

    # def delete(self, *args, **kwargs):
    #     obj = self.get_object()
    #     obj.is_deleted = True
    #     obj.save()
    #     return

# @api_view(['GET'])
# def product_list_view(request):
#     if request.method == 'GET':
#         products = Product.objects.order_by("created_at")
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#
# @api_view(["GET", "DELETE", "PUT"])
# def product_detail_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=404)
#
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     if request.method == "DELETE":
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     if request.method == "PUT":
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
