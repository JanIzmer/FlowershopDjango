from django.shortcuts import render
from .models import CartItem, Product, Cart
from Customer.models import Customer
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@require_POST
def place_order(request):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer)
    cart.add_to_order() 
    messages.success(request, "Zamówienie zostało złożone!")
    return redirect('cart_view')


@login_required
def cart_view(request):
    customer = Customer.objects.get(user=request.user)
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    return render(request, 'Cart/cart.html', {'cart_items': cart_items})


@login_required
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        product = get_object_or_404(Product, id=product_id)
        customer = Customer.objects.get(user=request.user)
        cart, created = Cart.objects.get_or_create(customer=customer)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1})
        if not created:
            item.quantity +=1
            item.save()
        return redirect('title')
    

@login_required
def remove_from_cart(request, product_id):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer)
    item = get_object_or_404(CartItem, id=product_id, cart=cart)
    item.delete()
    return redirect('cart_view')


@login_required
def decrease_quantity(request, product_id):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer)
    item = get_object_or_404(CartItem, id=product_id, cart=cart)
    if item.quantity >= 2:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart_view')

@login_required
def increase_quantity(request, product_id):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer)
    item = get_object_or_404(CartItem, id=product_id, cart=cart)
    item.quantity += 1
    item.save()
    return redirect('cart_view')

# Create your views here.
