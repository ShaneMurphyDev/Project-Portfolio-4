from django.contrib import admin
from .models import Subscription

# subscription view in admin
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)

admin.site.register(Subscription, SubscriptionAdmin)