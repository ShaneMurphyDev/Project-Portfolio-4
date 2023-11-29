from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from django.core.mail import send_mail
from django.conf import settings
from wildlyfe.settings import EMAIL_HOST_USER

# subscription view
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()

            # Send a confirmation email
            subject = 'Subscription Confirmation'
            message = (
                "Thank you for subscribing to our newsletter,"
                + " you will get updates for our future adventures!"
                + " Return to website: https://natureblog-2089d93a8eb1.herokuapp.com/"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [subscription.email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return render(request, 'subscription/success.html')
    else:
        form = SubscriptionForm()

    return render(request, 'subscription/subscribe.html', {'form': form})