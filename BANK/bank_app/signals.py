from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from .models import UserProfile, Transaction
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import OperationalError


# Signal to create a transaction after a user profile is updated
@receiver(post_save, sender=UserProfile)
def create_transaction_on_balance_update(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # Skip creating transaction if the profile is just created
        return

    try:
        # Fetch the previous balance from the database
        old_instance = UserProfile.objects.get(pk=instance.pk)
    except UserProfile.DoesNotExist:
        return

    # Check if the balance has changed
    if old_instance.balance != instance.balance:
        amount = instance.balance - old_instance.balance
        description = 'Credit' if amount > 0 else 'Debit'

        print(f"Balance updated for user: {instance.user.username}")
        print(f"Old balance: {old_instance.balance}, New balance: {instance.balance}")
        print(f"Transaction type: {description}, Amount: {abs(amount)}")

        Transaction.objects.create(
            user=instance.user,
            amount=abs(amount),
            balance_after=instance.balance,
            description=description
        )


# Signal to create superuser after migrations are applied
@receiver(post_migrate)
def create_superuser_after_migrate(sender, **kwargs):
    try:
        User = get_user_model()
        username = settings.SUPERUSER_NAME
        password = settings.SUPERUSER_PASSWORD

        # Check if the superuser already exists
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser {username}")
            User.objects.create_superuser(username=username, password=password)
        else:
            print(f"Superuser {username} already exists.")
    except OperationalError:
        print("Database not fully set up yet, skipping superuser creation.")
