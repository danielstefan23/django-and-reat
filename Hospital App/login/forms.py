from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'specializare', 'grupa_sanguina', 'job')

    def clean_email(self):
            email = self.cleaned_data.get('email')

            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return email

            raise forms.ValidationError(('Aceasta adresa de email este deja folosita!'), code = 'invalid')