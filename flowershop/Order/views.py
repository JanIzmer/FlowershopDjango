from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Customer.models import Customer
from Cart.models import Cart, CartItem
from django.views.decorators.http import require_POST
from .forms import CustomerForm

@login_required
def order_view(request):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_order')
    else:
        form = CustomerForm()
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    return render(request, 'order/order_view.html', {'cart_items': cart_items, 'form': form})


@require_POST
def place_order(request):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer)
    cart.add_to_order() 
    messages.success(request, "Zamówienie zostało złożone!")
    return redirect('cart_view')


