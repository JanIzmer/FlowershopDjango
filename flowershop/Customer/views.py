from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, CustomerAuthenticationForm, CustomerProfileForm
from Customer.models import Customer
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request):
    customer = Customer.objects.get(user=request.user)

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return render(request, 'Customer/profile.html', {'form': form, 'customer': customer})
    else:
        form = CustomerProfileForm(instance=customer)

    return render(request, 'Customer/profile.html', {'form': form, 'customer': customer})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'Customer/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomerAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('title')
    else:
        form = CustomerAuthenticationForm()
    return render(request, 'Customer/login.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


# Create your views here.
