from django.urls import path
from .views import order_view, place_order

urlpatterns = [
    path('order_view', order_view, name='order_view'),
    path('place_order', place_order, name='place_order')
]