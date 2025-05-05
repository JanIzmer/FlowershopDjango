from django.urls import path
from .views import order_view, order_history

urlpatterns = [
    path('order_view', order_view, name='order_view'),
    path('order_history', order_history, name='order_history')
]