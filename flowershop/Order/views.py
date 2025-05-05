from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Customer.models import Customer
from Cart.models import Cart, CartItem
from Order.models import Order
from .forms import CustomerForm
from django.core.mail import send_mail
from django.conf import settings

@login_required
def order_view(request):
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.filter(customer=customer).order_by('-created_at').first()
    cart = Cart.objects.get(customer=customer)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            cart.street = request.POST.get('street')
            cart.address = request.POST.get('address')
            cart.city = request.POST.get('city')
            cart.postal_code = request.POST.get('postal_code')
            cart.country = request.POST.get('country')
            form.save()
            cart.save()
            messages.success(request, "Dane zostały zaktualizowane!")
            cart.add_to_order() 
            messages.success(request, "Złożono zamówienie!")
            """ send_mail(
                subject='Dziękujemy za Twoje zamówienie 🌸',
                 message=(
                    'Dzień dobry,\n\n'
                    'Dziękujemy za złożenie zamówienia w naszej kwiaciarni! 🌷\n'
                    'Twoje zamówienie zostało pomyślnie przyjęte i wkrótce przystąpimy do jego realizacji.\n\n'
                    'Dołożymy wszelkich starań, aby kwiaty dotarły świeże, piękne i na czas.\n\n'
                    'W razie jakichkolwiek pytań lub wątpliwości, jesteśmy do Twojej dyspozycji:\n'
                    '📧 kontakt@flowershop.pl\n'
                    '📞 +48 123 456 789\n\n'
                    'Z kwiatowym pozdrowieniem,\n'
                    'Zespół FlowerShop 💐'
                ),
                from_email='Flowershop <jan.izmer@gmail.com>',
                recipient_list=['jann.izmer@gmail.com'],
                fail_silently=False,
                ) """
            return redirect('cart_view')
        else:
            print('Dane zostały nie zaktualizowane, forma nieporawna')
    else:
        form = CustomerForm(instance=customer)
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    return render(request, 'order/order_view.html', {'cart_items': cart_items, 'form': form, 'customer': customer, 'order': order, 'google_api_key': settings.GOOGLE_API_KEY})

@login_required
def order_history(request):
    customer = Customer.objects.get(user=request.user)
    order_list = Order.objects.filter(customer=customer)
    order_details=[]
    for order in order_list:
        products = order.get_order_products()  # Użycie metody get_order_products
        order_details.append({
            'order': order,
            'products': products
        })
    return render(request, 'order/order_history.html', {'order_details': order_details})



