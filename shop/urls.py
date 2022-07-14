from django.conf.urls import url
from django.urls import path, include

from .views import CategoryAPIView, ProductAPIView, SubCategoryAPIView, CustomerAPIView

urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('subcategory/', SubCategoryAPIView.as_view()),
    path('customer/', CustomerAPIView.as_view()),
    url(r'^chaining/', include('smart_selects.urls')),
]