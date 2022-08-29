from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import CommentModelViewSet, CategoryModelViewSet, \
    SubCategoryModelViewSet, ProductModelViewSet, OrderModelViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryModelViewSet)
router.register(r'sub_category', SubCategoryModelViewSet)
router.register(r'comment', CommentModelViewSet)
router.register(r'product', ProductModelViewSet)
router.register(r'order', OrderModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
]
