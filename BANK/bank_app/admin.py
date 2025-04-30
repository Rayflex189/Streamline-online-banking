from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number']  # Specify fields to display in the admin list
    search_fields = ['user__username']  #

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'balance_after', 'timestamp', 'description']  # Specify fields to display in the admin list
    search_fields = ['user__username', 'description']  # Search by user and description
    list_filter = ['timestamp', 'user']  # Add filters for timestamp and user
    ordering = ['-timestamp']
    

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('image_display')

    def image_display(self, obj):
        return obj.image.url if obj.image else None


