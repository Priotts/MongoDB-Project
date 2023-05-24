from django.shortcuts import render, redirect
from .forms import UserProfileForms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
import random

# Create your views here.

#USER AUTHENTICATION
def user_login (request): 
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)         
            messages.success(request, 'Login successful')
            return redirect ('user_profile')
        else:
            messages.error(request, 'Login failed')
    c_messages = messages.get_messages(request)
    return render(request, 'profile/user_login.html', {'c_messages': c_messages})

#USER LOGOUT
def logout_view (request):  
    logout(request)
    return redirect ('index')

#USER REGISTRATION
def sign_up (request):
    if request.method == 'POST':
        form = UserProfileForms(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User created')
            btc_amount = random.randint(1, 10) #random btc amount
            usd_amount = 10000 #usd amount
            UserProfile.objects.create(user=user, walletbtc=btc_amount, usd = usd_amount)
            messages.success(request, 'User created')
            return redirect('user_login')
        else:
            messages.error(request, 'User not created. Please check your data.')
            print(form.errors)
    else:
        form = UserProfileForms()
    c_messages = messages.get_messages(request)
    return render(request, 'profile/sign_up.html', {'form': form , 'c_messages': c_messages})

#USER PROFILE
@login_required
def user_profile (request):
    user = request.user
    return render(request, 'profile/user_profile.html', {'user': user})
