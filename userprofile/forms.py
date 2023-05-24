from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserProfileForms(UserCreationForm):
    # walletbtc = forms.FloatField()
    # usd = forms.FloatField()
    # profit = forms.FloatField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        exclude = ['walletbtc', 'usd', 'profit']