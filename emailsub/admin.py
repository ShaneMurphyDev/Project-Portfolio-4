from django.contrib import admin
from .models import Subscription

# Register your models here.
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    # Add a search box for the email field
    search_fields = ('email',)

admin.site.register(Subscription, SubscriptionAdmin)