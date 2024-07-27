from django.urls import path
from .views import LimitOrderListCreateView, LimitOrderRetrieveUpdateDestroyView, index


urlpatterns = [
    path('', index, name='index'),
    path('orders/', LimitOrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', LimitOrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]