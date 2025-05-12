
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings
from django.apps import apps
from .models import UserProfile, Transaction


@receiver(post_save, sender=UserProfile)
def create_transaction_on_balance_update(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # Skip transaction creation when profile is first created
        return

    try:
        old_instance = UserProfile.objects.get(pk=instance.pk)
    except UserProfile.DoesNotExist:
        return

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


@receiver(post_migrate)
def create_superuser_after_migrate(sender, **kwargs):
    # Ensure it's running only once and after all built-in apps are migrated
    if not apps.is_installed('django.contrib.contenttypes'):
        return

    from django.contrib.contenttypes.models import ContentType
    try:
        ContentType.objects.count()
    except Exception:
        return  # Abort if contenttypes table isn't ready yet

    User = get_user_model()
    username = settings.SUPERUSER_NAME
    password = settings.SUPERUSER_PASSWORD

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser {username}")
        User.objects.create_superuser(username=username, password=password)
    else:
        print(f"Superuser {username} already exists.")
