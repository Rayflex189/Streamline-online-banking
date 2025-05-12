from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout

from .decorators import *
from .models import *
from .utilis import *

# Create your views here.

login_required(login_url='LoginPage')
def pendingPro(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'bank_app/pendingPro.html', context)

@login_required(login_url='LoginPage')
def skrill(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['deposit_amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Create a transaction record without deducting the balance
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Balance remains unchanged
                            description='Debit'
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/skrill.html', context)

@login_required(login_url='LoginPage')
def Gcash(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['deposit_amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Create a transaction record without deducting the balance
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Balance remains unchanged
                            description='Debit'
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/Gcash.html', context)

login_required(login_url='LoginPage')
def trust_wise(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['deposit_amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Create a transaction record without deducting the balance
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Balance remains unchanged
                            description='Debit'
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/wise.html', context)

login_required(login_url='LoginPage')
def western_union(request): 
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['deposit_amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Remove balance deduction logic
                        # Create a transaction record
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Keep the balance as is
                            description='Debit'  # Change description if needed (e.g., Deposit instead of )
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/western_union.html', context)

login_required(login_url='LoginPage')
def payoneer(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Remove balance deduction logic
                        # Create a transaction record
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Keep the balance as is
                            description='Debit'  # Change description if needed (e.g., Deposit instead of Debit)
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/payoneer.html', context)

login_required(login_url='LoginPage')
def bank_transfer(request): 
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['deposit_amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Create a transaction record without deducting the balance
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Balance remains unchanged
                            description='Debit'
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/bank_transfer.html', context)

login_required(login_url='LoginPage')
def crypto(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['deposit_amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Create a transaction record without deducting the balance
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Balance remains unchanged
                            description='Debit'
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/crypto.html', context)

@login_required(login_url='loginview')
def paypal(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                if not user_profile.is_linked:
                    form.add_error(None, "Please activate your account before making a deposit.")
                else:
                    deposit_amount = form.cleaned_data['deposit_amount']
                    if deposit_amount <= 0:
                        form.add_error('amount', "Deposit amount must be greater than zero.")
                    else:
                        # Create a transaction record without deducting the balance
                        Transaction.objects.create(
                            user=user_profile.user,
                            amount=deposit_amount,
                            balance_after=user_profile.balance,  # Balance remains unchanged
                            description='Debit'
                        )

                        return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'bank_app/paypal.html', context)

def home(request):
    return render(request, 'bank_app/landing.html')

@login_required(login_url='LoginPage')
def dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    # Fetch the last 10 transactions
    transactions = Transaction.objects.filter(user=user_profile.user).order_by('-timestamp')[:10]
    balance = user_profile.balance
    currency = user_profile.currency
    account_type = user_profile.account_type
    context = {'currency':currency, 'balance':balance, 'user_profile':user_profile, 'transactions':transactions, 'account_type':account_type}
    return render(request, 'bank_app/dashboard.html', context)


@unauthenticated_user
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('LoginPage')

    context = {'form': form}
    return render(request, 'bank_app/register.html', context)


@unauthenticated_user
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('reset_setting')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'bank_app/login.html')

@login_required(login_url='LoginPage')
def profile_setting(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/profile_settings.html', context)

@login_required(login_url='LoginPage')
def aml(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/aml.html')

@login_required(login_url='LoginPage')
def imf(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = IMFForm(request.POST)
        if form.is_valid():
            imf_code_input = form.cleaned_data['imf']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_imf(imf_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('pending')
            else:
                form.add_error(None, 'Invalid IMF code')
    else:
        form = IMFForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'bank_app/imf.html', context)

@login_required(login_url='LoginPage')
def tac(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/tac.html')

@login_required(login_url='LoginPage')
def kyc(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    # Account upgrade status message
    if user_profile.is_upgraded:
        message = 'Account upgraded successfully'
    else:
        message = 'Account upgrade processing. Contact support for more information.'

    # Months and years for dropdowns
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    current_year = datetime.now().year
    years = [str(year) for year in range(current_year, current_year + 10)]

    # If the form is submitted via POST
    if request.method == "POST":
        # Get form data
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        expiry_date = request.POST.get('expiry_date')

        # Validate inputs
        if user_profile.card_number != card_number:
            messages.error(request, 'Invalid card number. Please check and try again.')
            return redirect('kyc')

        if user_profile.cvv != cvv:
            messages.error(request, 'Invalid CVV. Please check and try again.')
            return redirect('kyc')

        if user_profile.expiry_date != expiry_date:
            messages.error(request, 'Invalid expiration date. Please check and try again.')
            return redirect('kyc')

        # Update profile
        user_profile.is_upgraded = True
        user_profile.save()

        messages.success(request, 'Account upgraded successfully!')
        return redirect('pendingPro')

    # Context to render on the page (only runs if not redirected above)
    context = {
        'user_profile': user_profile,
        'message': message,
        'months': months,
        'years': years,
    }
    return render(request, 'bank_app/kyc.html', context)

@login_required(login_url='LoginPage')
def statistics(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/statistics.html', context)

@login_required(login_url='LoginPage')
def alert(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/alert.html', context)

@login_required(login_url='LoginPage')
def transaction_details(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/transaction_details.html')

@login_required(login_url='LoginPage')
def pending(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/pending.html')

@login_required(login_url='LoginPage')
def loans(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'bank_app/loans.html', context)

@login_required(login_url='LoginPage')
@transaction.atomic
def reset_setting(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
            form = UserProfileForm(request.POST,request.FILES, instance=request.user.userprofile)
            if form.is_valid():
                form.save()
                return redirect('dashboard')  # Redirect to the same page after successful update
            else:
                form = UserProfileForm(instance=request.user.userprofile)

    context = {
                'form': form
            }
    return render(request, 'bank_app/reset_setting.html', context)

@login_required(login_url='LoginPage')
@transaction.atomic
def linking_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = LinkingCodeForm(request.POST)
        if form.is_valid():
            # Check if the linking code matches
            entered_code = form.cleaned_data['linking_code']
            if entered_code == profile.linking_code:
                messages.success(request, 'Account successfully linked.')
                # Handle linking logic here, e.g., set a flag in UserProfile
                profile.is_linked = True
                profile.save()
                return redirect('dashboard')  # Redirect to dashboard or another view
            else:
                messages.error(request, 'Invalid linking code. Please try again.')
        else:
            messages.error(request, 'Form validation failed. Please check the input.')

    else:
        form = LinkingCodeForm()

    context = {
        'form': form,
        'user_profile': profile
    }
    return render(request, 'bank_app/linking_page.html', context)


@login_required(login_url='LoginPage')
def LogOut(request):
    logout(request)
    return redirect('LoginPage')