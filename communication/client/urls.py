from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# FIX → Remove trailing slash here
router = DefaultRouter()
router.register('orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    # Product APIs
    path('products/', views.ProductListCreateAPIView.as_view(), name="product-list-create"),
    # path('products/detail/<int:id>/', views.ProductDetailAPIView.as_view()),  
    # path('products/destroy/<int:id>/', views.ProductDestroyAPIView.as_view()),  

    # JWT Authentication APIs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Add router-generated URLs at the end
urlpatterns += router.urls

