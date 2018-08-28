from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    """Render the index.html page"""
    return render(request, 'index.html')

@login_required
def user_logout(request):
    """Log user out"""
    auth.logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect(reverse('index'))

def user_login(request):
    """Log user in """
    if request.user.is_authenticated:
        return redirect(reverse('index')) 
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid:
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in. Welcome!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'There was a problem with your credentials, please try again')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form" : login_form})

def user_registration(request):
    """Render registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password2'])
            if user:
                auth.login(request=request, user=user)
                messages.success(request, 'You are now registered!')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'You are now registered!') 
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {'registration_form' : registration_form})

def user_profile(request):
    """Render user profile"""
    user_profile = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'user_profile' : user_profile})