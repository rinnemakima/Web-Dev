from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductByCategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'categories/(?P<id>\d+)/products', ProductByCategoryViewSet, basename='products-by-category')

urlpatterns = [
    path('', views.getDatainclude(router.urls)),
]

