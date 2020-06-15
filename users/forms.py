from django import forms
from . models import Account
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'mobile_number', 'email', 'password1', 'password2', 'delivery_address', 'plan']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['plan']
