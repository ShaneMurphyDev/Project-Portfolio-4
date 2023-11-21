from .models import Comment, Subscription
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']