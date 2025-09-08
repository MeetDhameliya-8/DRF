from django.shortcuts import get_object_or_404


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


from client.serializers import ProductSerializer, OrderSerializer, OrderItemSerializer
from client.models import Product, Order, OrderItem
from client.filters import ProductFilter, InStockFilterBackend





class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [ 
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        InStockFilterBackend
    ]
    filterset_fields = ('name','price') 

    @method_decorator(cache_page(60 * 15, key_prefix='product_list'))
    def list(self, request, *args, **kwargs):
         return super().list(request, *args, **kwargs)
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()   




class OrderViewSet(viewsets.ModelViewSet):
      queryset = Order.objects.prefetch_related('products')
      serializer_class = OrderSerializer
      permission_classes = [AllowAny]
      pagination_class= None


 























'''class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items_product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs =   super().get_queryset()
        return qs.filter(user=self.request.user)



class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'id'
'''

