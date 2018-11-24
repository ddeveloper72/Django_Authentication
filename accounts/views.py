from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserloginForm

# Create your views here.

def index(request):
    """return the index.html file"""
    
    return render(request, 'index.html')

@login_required # Checks to see if a user is loged in BEFORE running the logout function.   
def logout(request):
    """Log the user out"""
    
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('index'))

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index')) 
        # security which prevents access to the login page via url bar

    if request.method == "POST": 
        login_form = UserloginForm(request.POST)

        if login_form.is_valid():
            user =  auth.authenticate(username=request.POST['username'],
                                      password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your login is sucessfull!")
                return redirect(reverse('index'))
                # security which prevents access to the login page via url bar

            else:
                login_form.add_error(None, "Your username or password is incorrect")

    else:
        login_form = UserloginForm()

    return render(request, 'login.html', {"login_form": login_form})

def registration(request):
    """Render the registration page"""
    return render(request, 'registration.html')