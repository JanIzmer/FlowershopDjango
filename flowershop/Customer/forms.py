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
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class CustomerAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label = 'Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
