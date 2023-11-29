from django import forms
from .models import Subscription

# subscription form
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']