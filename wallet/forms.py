# Import forms
from django import forms

from .models import Wallet

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ('user_id', 'balance', 'monetary_unit')