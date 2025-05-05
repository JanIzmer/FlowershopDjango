from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'secondname', 'phone', 'email', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'firstname': 'Imię',
            'secondname': 'Nazwisko',
            'phone': 'Numer telefonu',
            'email': 'Adres e-mail',
            'address': 'Adres dostawy',
        }