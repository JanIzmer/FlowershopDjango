from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, decrease_quantity, increase_quantity

urlpatterns = [
    path('mycart', cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/decrease_quantity/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/increase_quantity/<int:product_id>/', increase_quantity, name='increase_quantity')

]