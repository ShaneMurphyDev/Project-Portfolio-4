from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from django.core.mail import send_mail
from django.conf import settings
from wildlyfe.settings import EMAIL_HOST_USER

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()

            # Send a confirmation email
            subject = 'Subscription Confirmation'
            message = 'Thank you for subscribing to the Wildlyfe newsletter!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [subscription.email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return render(request, 'subscription/success.html')
    else:
        form = SubscriptionForm()

    return render(request, 'subscription/subscribe.html', {'form': form})