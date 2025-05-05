from django import forms
from .models import Customer,User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(label="Powrórz hasło", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =["username", "email", "password"]
    def cleanPassword(self):
        if self.cleaned_data["password"]!=self.cleaned_data["password2"]:
            raise forms.ValidationError("Hasła nie są zgodne")
        else:
            return self.cleaned_data["password"]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class CustomerAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa użytkownika'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'})
    )

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'secondname', 'phone', 'address']
